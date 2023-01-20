from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union
import pandas as pd
from datetime import datetime, timezone

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
    #df["STOPTIME"].iloc[0:1] = df["STOPTIME"].iloc[0:1].fillna(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    df["STOPTIME"].iloc[0:1] = datetime(2022, 10, 30, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
    df["STARTTIME"] = pd.to_datetime(df["STARTTIME"], utc=True)
    df["STOPTIME"] = pd.to_datetime(df["STOPTIME"], utc=True)
    df["DURATION"] = (pd.to_datetime(df["STOPTIME"]) - pd.to_datetime(df["STARTTIME"])).dt.total_seconds().astype(int)
    df = df[["USERNAME",
             "STARTTIME",
             "STOPTIME",
             "DURATION",
             "TOTALUSAGE"]]
    df = df.rename(columns = {"USERNAME": "ND",
                              "STARTTIME": "START_DATE",
                              "STOPTIME": "END_DATE",
                              "TOTALUSAGE": "TOTAL_USAGE_BYTE"})
    df["DURATION_HOUR"] = round(df["DURATION"] / 3600).astype(int)
    df["USAGE/HOUR_BYTE"] = df["TOTAL_USAGE_BYTE"] * 3600 / df["DURATION"]
    df = df.loc[df["DURATION"] > 0]

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    print(year, month, day)
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
        id = 0
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
        dict["total_usage_byte"] = df["TOTAL_USAGE_BYTE"].iloc[i].tolist()
        dict["duration_hour"] = df["DURATION_HOUR"].iloc[i].tolist()
        dict["usage_hour_byte"] = df["USAGE/HOUR_BYTE"].iloc[i].tolist()
        list_df.append(dict)

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
        
        print("Gangguan :", df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] < 80000000)].sum(), "detik")
        dict["gangguan"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] < 80000000)].sum().tolist()
        print("Low Usage :", df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 80000000) &
                                                     (df_temp["USAGE/HOUR_BYTE"] < 100000000)].sum(), "detik")
        dict["low_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 80000000) &
                                                  (df_temp["USAGE/HOUR_BYTE"] < 100000000)].sum().tolist()
        print("Med Usage :", df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 100000000) &
                                                     (df_temp["USAGE/HOUR_BYTE"] < 1000000000)].sum(), "detik")
        dict["med_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 100000000) &
                                                  (df_temp["USAGE/HOUR_BYTE"] < 1000000000)].sum().tolist()
        print("High Usage :", df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 1000000000)].sum(), "detik")
        dict["high_usg"] = df_temp["DURATION"].loc[(df_temp["USAGE/HOUR_BYTE"] >= 1000000000)].sum().tolist()
        list_obj.append(dict)
    print(df[["START_DATE", "END_DATE", "DURATION_HOUR", "USAGE/HOUR_BYTE"]])
    return {"detail": list_df, 
            "summary": list_obj}
