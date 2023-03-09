from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
import pandas as pd
import numpy as np
from datetime import datetime, timezone, timedelta
import math

app = FastAPI()

class Data(BaseModel):
    USERNAME: Union[str, None]
    CLID: Union[str, None]
    FRAMEIPV6ADDRESS: Union[str, None]
    FRAMEIPADDRESS: Union[str, None]
    INPUT_OKTET: Union[int, None]
    OUTPUT_OKTET: Union[int, None]
    STARTTIME: Union[str, None]
    STOPTIME: Union[str, None]
    TERMINATECAUSE: Union[str, None]
    TOTALUSAGE: Union[int, None]
    USAGETIME: Union[int, None]
    STATUSKONEKSI: Union[str, None]

def converter(time):
    if int(np.floor(time / (3600*24))) != 0:
        time = np.round(time / (3600*24), 2)
        unit = "hari"
    elif int(np.floor(time / (3600))) != 0:
        time = np.round(time / (3600), 2)
        unit = "jam"
    elif int(np.floor(time / (60))) != 0:
        time = np.round(time / (60), 2)
        unit = "menit"
    else:
        unit = "detik"
            
    return time, unit

@app.get("/predict")
def predict(data: List[Data]):
    def Convert(tup, dict):
        for a, b in tup:
            dict.setdefault(a, b)
        return dict
    
    data_temp = []
    for i in range(len(data)):
        dictionary = {}
        data_temp.append(Convert(list(data[i]), dictionary))
    df = pd.DataFrame.from_records(data_temp)

    df["USERNAME"] = df["USERNAME"].apply(lambda x: x[:-11])
    if df["STOPTIME"].iloc[0:1].isnull().all() == True:
        df["STOPTIME"].iloc[0:1] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    df["STARTTIME"] = pd.to_datetime(df["STARTTIME"], utc=True)
    df["STOPTIME"] = pd.to_datetime(df["STOPTIME"], utc=True)
    
    if df["STOPTIME"].values[0] < pd.Timestamp('today'):
        new_row = {"USERNAME": df["USERNAME"].iloc[0],
                   "STARTTIME": (df["STOPTIME"].iloc[0:1] + timedelta(seconds = 1)).values[0], 
                   "STOPTIME": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                   "TOTALUSAGE": 0}
        df = df.append(new_row, ignore_index=True)
    df["STARTTIME"] = pd.to_datetime(df["STARTTIME"], utc=True)
    df["STOPTIME"] = pd.to_datetime(df["STOPTIME"], utc=True)

    df["DURATION"] = (pd.to_datetime(df["STOPTIME"]) - pd.to_datetime(df["STARTTIME"])).dt.total_seconds().astype(int)
    df = df.sort_values(by = "STOPTIME", ascending = False).reset_index(drop = True)
    df = df[["USERNAME",
             "STARTTIME",
             "STOPTIME",
             "DURATION",
             "TOTALUSAGE"]]
    #print(df)
    df = df.rename(columns = {"USERNAME": "ND",
                              "STARTTIME": "START_DATE",
                              "STOPTIME": "END_DATE",
                              "TOTALUSAGE": "TOTAL_USAGE_BYTE"})
    df["DURATION_HOUR"] = round(df["DURATION"] / 3600).astype(int)
    df["DURATION_SECOND"] = df["DURATION"].astype(int)
    df["USAGE/HOUR_BYTE"] = df["TOTAL_USAGE_BYTE"] * 3600 / df["DURATION"]
    df = df.loc[df["DURATION"] > 0]

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    #print(year, month, day)
    if day <= 10:
        if month != 1:
    	    list_date = [datetime(year, month - 1, 11, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month - 1, 21, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 11, 0, 0, 0, tzinfo=timezone.utc)]
        else:
            list_date = [datetime(year, 12, 11, 0, 0, 0, tzinfo=timezone.utc), datetime(year, 12, 21, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 11, 0, 0, 0, tzinfo=timezone.utc)]
    elif day > 10 and day <= 20:
        if month != 1:
    	    list_date = [datetime(year, month - 1, 21, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 11, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 21, 0, 0, 0, tzinfo=timezone.utc)]
        else:
    	    list_date = [datetime(year, 12, 21, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 11, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 21, 0, 0, 0, tzinfo=timezone.utc)]
    else:
    	list_date = [datetime(year, month, 1, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 11, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month, 21, 0, 0, 0, tzinfo=timezone.utc), datetime(year, month + 1, 1, 0, 0, 0, tzinfo=timezone.utc)]
    
    list_df = []
    for i in range(len(df)):
        dict = {}
        retry = True
        for j in range(3):
            if len(df.iloc[i:i+1].loc[(df["END_DATE"] >= list_date[j]) &
                                      (df["START_DATE"] < list_date[j+1])]) > 0:
                id = j+1
                dict["id"] = id
                if len(df.iloc[i:i+1].loc[(df["USAGE/HOUR_BYTE"] < 80000000)]) > 0:
                    desc = "gangguan"
                elif len(df.iloc[i:i+1].loc[(df["USAGE/HOUR_BYTE"] >= 80000000) &
                                            (df["USAGE/HOUR_BYTE"] < 100000000)]) > 0:
                    desc = "low_usg"
                elif len(df.iloc[i:i+1].loc[(df["USAGE/HOUR_BYTE"] >= 100000000) &
                                            (df["USAGE/HOUR_BYTE"] < 1000000000)]) > 0:
                    desc = "med_usg"
                else:
                    desc = "high_usg"
                dict["desc"] = desc
                dict["nd"] = df["ND"].iloc[i]
                dict["start_date"] = df["START_DATE"].iloc[i]
                dict["end_date"] = df["END_DATE"].iloc[i]
                dict["duration"] = df["DURATION"].iloc[i].tolist()
                dict["duration"], dict["unit_duration"] = converter(dict["duration"])
                dict["total_usage_byte"] = df["TOTAL_USAGE_BYTE"].iloc[i].tolist()
                dict["duration_hour"] = df["DURATION_HOUR"].iloc[i].tolist()
                dict["duration_second"] = df["DURATION_SECOND"].iloc[i].tolist()
                dict["usage_hour_byte"] = df["USAGE/HOUR_BYTE"].iloc[i].tolist()
                if retry == True:
                    list_df.append(dict)
                else:
                    continue
                retry = False
                # Change it, need to separate the date

    list_obj = []
    for i in range(3):
        dict = {}
        dict["id"] = i+1
        dict["desc"] = "{}-{} hari kebelakang".format((2-i)*10, (3-i)*10)
        print("Segment {}".format(i+1))
        df_temp = df.loc[(df["END_DATE"] >= list_date[i]) &
                         (df["START_DATE"] < list_date[i+1])].copy()
        df_temp["USAGE/HOUR_BYTE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)] = ((df_temp["USAGE/HOUR_BYTE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)] * (df_temp["END_DATE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)] - df_temp["START_DATE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)]).dt.total_seconds()) / (df_temp["END_DATE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)] - list_date[i]).dt.total_seconds())
        df_temp["START_DATE"].loc[((df_temp["START_DATE"] - list_date[i]).dt.total_seconds() < 0)] = list_date[i]
        df_temp["USAGE/HOUR_BYTE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)] = ((df_temp["USAGE/HOUR_BYTE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)] * (df_temp["END_DATE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)] - df_temp["START_DATE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)]).dt.total_seconds()) / (df_temp["END_DATE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)] - list_date[i+1]).dt.total_seconds())
        df_temp["END_DATE"].loc[((list_date[i+1] - df_temp["END_DATE"]).dt.total_seconds() < 0)] = list_date[i+1]
        
        dict["gangguan"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] < 80000000)].sum().tolist()
        dict["low_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 80000000) &
                                                  (df_temp["USAGE/HOUR_BYTE"] < 100000000)].sum().tolist()
        dict["med_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 100000000) &
                                                  (df_temp["USAGE/HOUR_BYTE"] < 1000000000)].sum().tolist()
        dict["high_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 1000000000)].sum().tolist()
        
        dict["gangguan"], dict["unit_gangguan"] = converter(dict["gangguan"])
        dict["low_usg"], dict["unit_low_usg"] = converter(dict["low_usg"])
        dict["med_usg"], dict["unit_med_usg"] = converter(dict["med_usg"])
        dict["high_usg"], dict["unit_high_usg"] = converter(dict["high_usg"])
        print("Gangguan :", dict["gangguan"], dict["unit_gangguan"])
        print("Low Usage :", dict["low_usg"], dict["unit_low_usg"])
        print("Medium Usage :", dict["med_usg"], dict["unit_med_usg"])
        print("High Usage :", dict["high_usg"], dict["unit_high_usg"])
        list_obj.append(dict)

    return {"detail": list_df, 
            "summary": list_obj}