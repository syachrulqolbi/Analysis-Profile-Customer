# Analysis Profile Customer (Single)

## Data
Data Usage Customer, feature used in the model:
* USERNAME
* CLID
* FRAMEIPV6ADDRESS
* FRAMEIPADDRESS
* INPUT_OKTET
* OUTPUT_OKTET
* STARTTIME
* STOPTIME
* TERMINATECAUSE
* TOTALUSAGE
* USAGETIME
* STATUSKONEKSI

## Team Member
1. Syachrul Qolbi Nur Septi

## Table of Contents
1. [Requirements](#requirements) to install on your system
2. [Tutorial](#tutorial)

## Requirements

The main requirements are listed below:

Tested with 
* Python 3.7.10
* Pandas 1.1.5

Additional requirements to generate dataset:

* FastAPI
* Pydantic

## Tutorial
# Instalasi Python

Pastikan sudah terinstall python dan pip dalam system anda, jika system anda mengunakan linux bisa mengikuti command di bawah ini

`
sudo apt install python3-pip
`

jika system mengunakan OS windows atau yang lain bisa minjau situs resmi python untuk instalasi python https://www.python.org/downloads/

# Instalasi Dependency 
Agar code dapat berjalan di perlukan beberapa dependecy, dapat langsung menjalankan command di terminal berikut satu demi satu jika python dan pip sudah terinstall

```
pip install fastapi
pip install uvicorn
```

# Menjalankan API
Untuk menjalankan API cukup mejalankan command berikut di terminal
```
uvicorn main:app --reload
```
Secara default dia akan jalan secara lokal di 127.0.0.1 dengan port 8000 

Output jika runnning berhasil

![image](/Images/Output_Uvicorn.png) 

Jika ingin di jalankan di port dan address host yang berbeda bisa mengunakan option --host dan --port
```
uvicorn --host [host address] --port [nilai port]  main:app --reload 
```

# Menggunakan API
Kita akan memprediksi status berlangganan user, apakah user tersebut akan berlangganan kembali di bulan depan atau tidak. Untuk mengunakan endpoint bisa dengan menyiapkan body parameternya berupa format JSON dengan format seperti berikut

```
[
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4025:2e41::/64",
        "FRAMEIPADDRESS": "10.45.29.242",
        "INPUT_OKTET": null,
        "OUTPUT_OKTET": null,
        "STARTTIME": "2022-10-28 12:09:12+07",
        "STOPTIME": null,
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 1073741824,
        "USAGETIME": 17174252,
        "STATUSKONEKSI": "Interim-Update"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-28 12:01:12+07",
        "STOPTIME": "2022-10-28 12:09:11+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 479,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402a:12bd::/64",
        "FRAMEIPADDRESS": "36.65.122.15",
        "INPUT_OKTET": 165328710,
        "OUTPUT_OKTET": 2495390669,
        "STARTTIME": "2022-10-28 05:31:41+07",
        "STOPTIME": "2022-10-28 12:01:11+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 2660719379,
        "USAGETIME": 23370000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-28 02:03:38+07",
        "STOPTIME": "2022-10-28 05:31:40+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 12482,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402a:1d1a::/64",
        "FRAMEIPADDRESS": "36.65.127.69",
        "INPUT_OKTET": 257316024,
        "OUTPUT_OKTET": 4033615809,
        "STARTTIME": "2022-10-27 18:35:37+07",
        "STOPTIME": "2022-10-28 02:03:37+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 4290931833,
        "USAGETIME": 26880000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-27 18:33:59+07",
        "STOPTIME": "2022-10-27 18:35:36+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 97,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4029:26d9::/64",
        "FRAMEIPADDRESS": "10.45.93.157",
        "INPUT_OKTET": 1032377210,
        "OUTPUT_OKTET": 6521829332,
        "STARTTIME": "2022-10-27 05:15:57+07",
        "STOPTIME": "2022-10-27 18:33:58+07",
        "TERMINATECAUSE": "User-Request",
        "TOTALUSAGE": 7554206542,
        "USAGETIME": 47881000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-27 02:56:32+07",
        "STOPTIME": "2022-10-27 05:15:56+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 8364,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402b:2699::/64",
        "FRAMEIPADDRESS": "10.45.115.113",
        "INPUT_OKTET": 807275560,
        "OUTPUT_OKTET": 12226121708,
        "STARTTIME": "2022-10-26 12:20:00+07",
        "STOPTIME": "2022-10-27 02:56:31+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 13033397268,
        "USAGETIME": 52591000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-26 09:14:17+07",
        "STOPTIME": "2022-10-26 12:19:59+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 11142,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4027:272c::/64",
        "FRAMEIPADDRESS": "10.45.52.98",
        "INPUT_OKTET": 998762081,
        "OUTPUT_OKTET": 15803426144,
        "STARTTIME": "2022-10-25 05:10:43+07",
        "STOPTIME": "2022-10-26 09:14:16+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 16802188225,
        "USAGETIME": 101013000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-25 01:32:12+07",
        "STOPTIME": "2022-10-25 05:10:42+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 13110,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402b:1253::/64",
        "FRAMEIPADDRESS": "125.163.45.80",
        "INPUT_OKTET": 244402323,
        "OUTPUT_OKTET": 4112098512,
        "STARTTIME": "2022-10-24 19:29:40+07",
        "STOPTIME": "2022-10-25 01:32:11+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 4356500835,
        "USAGETIME": 21751000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-24 19:28:47+07",
        "STOPTIME": "2022-10-24 19:29:39+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 52,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402b:2001::/64",
        "FRAMEIPADDRESS": "10.45.116.154",
        "INPUT_OKTET": 768666692,
        "OUTPUT_OKTET": 8427783569,
        "STARTTIME": "2022-10-24 05:27:51+07",
        "STOPTIME": "2022-10-24 19:28:46+07",
        "TERMINATECAUSE": "User-Request",
        "TOTALUSAGE": 9196450261,
        "USAGETIME": 50455000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-23 23:46:14+07",
        "STOPTIME": "2022-10-24 05:27:50+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 20496,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402f:1d6d::/64",
        "FRAMEIPADDRESS": "10.45.160.65",
        "INPUT_OKTET": 1012480351,
        "OUTPUT_OKTET": 20578225823,
        "STARTTIME": "2022-10-23 07:16:42+07",
        "STOPTIME": "2022-10-23 23:46:13+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 21590706174,
        "USAGETIME": 59371000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-23 04:33:05+07",
        "STOPTIME": "2022-10-23 07:16:41+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 9816,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4020:1a86::/64",
        "FRAMEIPADDRESS": "36.65.3.227",
        "INPUT_OKTET": 993557385,
        "OUTPUT_OKTET": 27112778201,
        "STARTTIME": "2022-10-22 07:11:34+07",
        "STOPTIME": "2022-10-23 04:33:04+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 28106335586,
        "USAGETIME": 76890000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-22 02:02:01+07",
        "STOPTIME": "2022-10-22 07:11:33+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 18572,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4022:1fd7::/64",
        "FRAMEIPADDRESS": "125.164.184.122",
        "INPUT_OKTET": 349513955,
        "OUTPUT_OKTET": 8559828347,
        "STARTTIME": "2022-10-21 18:40:30+07",
        "STOPTIME": "2022-10-22 02:02:00+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 8909342302,
        "USAGETIME": 26490000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-21 18:31:21+07",
        "STOPTIME": "2022-10-21 18:40:29+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 548,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4027:2ef2::/64",
        "FRAMEIPADDRESS": "10.45.58.161",
        "INPUT_OKTET": 1716328160,
        "OUTPUT_OKTET": 39661905853,
        "STARTTIME": "2022-10-20 14:20:48+07",
        "STOPTIME": "2022-10-21 18:31:20+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 41378234013,
        "USAGETIME": 101432000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-20 14:20:39+07",
        "STOPTIME": "2022-10-20 14:20:47+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 8,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4022:1571::/64",
        "FRAMEIPADDRESS": "125.164.182.67",
        "INPUT_OKTET": 6049598483,
        "OUTPUT_OKTET": 103911657208,
        "STARTTIME": "2022-10-16 05:31:05+07",
        "STOPTIME": "2022-10-20 14:20:38+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 109961255691,
        "USAGETIME": 377373000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-16 04:49:24+07",
        "STOPTIME": "2022-10-16 05:31:04+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 2500,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402b:2249::/64",
        "FRAMEIPADDRESS": "10.45.120.127",
        "INPUT_OKTET": 4729375622,
        "OUTPUT_OKTET": 42990000177,
        "STARTTIME": "2022-10-14 10:13:52+07",
        "STOPTIME": "2022-10-16 04:49:23+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 47719375799,
        "USAGETIME": 153331000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-14 09:43:00+07",
        "STOPTIME": "2022-10-14 10:13:51+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 1851,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4029:2e08::/64",
        "FRAMEIPADDRESS": "10.45.88.174",
        "INPUT_OKTET": 1090501674,
        "OUTPUT_OKTET": 17878273970,
        "STARTTIME": "2022-10-13 04:58:28+07",
        "STOPTIME": "2022-10-14 09:42:59+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 18968775644,
        "USAGETIME": 103471000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-13 04:31:20+07",
        "STOPTIME": "2022-10-13 04:58:27+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 1627,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4027:1d69::/64",
        "FRAMEIPADDRESS": "36.65.66.238",
        "INPUT_OKTET": 861940335,
        "OUTPUT_OKTET": 19789317494,
        "STARTTIME": "2022-10-11 22:22:49+07",
        "STOPTIME": "2022-10-13 04:31:19+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 20651257829,
        "USAGETIME": 108510000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-11 22:22:24+07",
        "STOPTIME": "2022-10-11 22:22:48+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 24,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPADDRESS": "125.166.185.254",
        "INPUT_OKTET": 577109209,
        "OUTPUT_OKTET": 14175150041,
        "STARTTIME": "2022-10-11 04:54:53+07",
        "STOPTIME": "2022-10-11 22:22:23+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 14752259250,
        "USAGETIME": 62850000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-11 01:49:44+07",
        "STOPTIME": "2022-10-11 04:54:52+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 11108,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4025:1076::/64",
        "FRAMEIPADDRESS": "36.65.230.247",
        "INPUT_OKTET": 1612560514,
        "OUTPUT_OKTET": 29426848938,
        "STARTTIME": "2022-10-09 16:14:12+07",
        "STOPTIME": "2022-10-11 01:49:43+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 31039409452,
        "USAGETIME": 120931000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-09 16:11:47+07",
        "STOPTIME": "2022-10-09 16:14:11+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 144,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4023:152f::/64",
        "FRAMEIPADDRESS": "125.166.143.44",
        "INPUT_OKTET": 517574059,
        "OUTPUT_OKTET": 8048340864,
        "STARTTIME": "2022-10-09 05:30:15+07",
        "STOPTIME": "2022-10-09 16:11:46+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 8565914923,
        "USAGETIME": 38491000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-09 04:53:07+07",
        "STOPTIME": "2022-10-09 05:30:14+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 2227,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402b:19d3::/64",
        "FRAMEIPADDRESS": "125.163.36.190",
        "INPUT_OKTET": 1554565298,
        "OUTPUT_OKTET": 18078070386,
        "STARTTIME": "2022-10-08 06:35:34+07",
        "STOPTIME": "2022-10-09 04:53:06+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 19632635684,
        "USAGETIME": 80252000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-07 22:07:12+07",
        "STOPTIME": "2022-10-08 06:35:33+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 30501,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4029:2fd6::/64",
        "FRAMEIPADDRESS": "10.45.90.88",
        "INPUT_OKTET": 887897477,
        "OUTPUT_OKTET": 20110052586,
        "STARTTIME": "2022-10-06 05:40:40+07",
        "STOPTIME": "2022-10-07 22:07:11+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 20997950063,
        "USAGETIME": 145591000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-05 23:21:32+07",
        "STOPTIME": "2022-10-06 05:40:39+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 22747,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4028:208b::/64",
        "FRAMEIPADDRESS": "10.45.72.89",
        "INPUT_OKTET": 389892008,
        "OUTPUT_OKTET": 8313034571,
        "STARTTIME": "2022-10-05 04:54:00+07",
        "STOPTIME": "2022-10-05 23:21:31+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 8702926579,
        "USAGETIME": 66451000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-04 23:16:28+07",
        "STOPTIME": "2022-10-05 04:53:59+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 20251,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4024:161c::/64",
        "FRAMEIPADDRESS": "125.166.184.121",
        "INPUT_OKTET": 979797131,
        "OUTPUT_OKTET": 27481319105,
        "STARTTIME": "2022-10-04 05:01:55+07",
        "STOPTIME": "2022-10-04 23:16:27+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 28461116236,
        "USAGETIME": 65672000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-04 00:46:08+07",
        "STOPTIME": "2022-10-04 05:01:54+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 15346,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4028:226b::/64",
        "FRAMEIPADDRESS": "10.45.70.104",
        "INPUT_OKTET": 902219999,
        "OUTPUT_OKTET": 12102398153,
        "STARTTIME": "2022-10-03 05:11:36+07",
        "STOPTIME": "2022-10-04 00:46:07+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 13004618152,
        "USAGETIME": 70471000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-03 01:15:05+07",
        "STOPTIME": "2022-10-03 05:11:35+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 14190,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4026:1b79::/64",
        "FRAMEIPADDRESS": "36.65.54.195",
        "INPUT_OKTET": 1014876164,
        "OUTPUT_OKTET": 17478167447,
        "STARTTIME": "2022-10-02 08:51:33+07",
        "STOPTIME": "2022-10-03 01:15:04+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 18493043611,
        "USAGETIME": 59011000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-02 07:55:53+07",
        "STOPTIME": "2022-10-02 08:51:32+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 3339,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:4022:1403::/64",
        "FRAMEIPADDRESS": "125.164.176.26",
        "INPUT_OKTET": 45504098,
        "OUTPUT_OKTET": 1360814849,
        "STARTTIME": "2022-10-02 07:08:22+07",
        "STOPTIME": "2022-10-02 07:55:52+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 1406318947,
        "USAGETIME": 2850000,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": null,
        "FRAMEIPADDRESS": null,
        "INPUT_OKTET": 0,
        "OUTPUT_OKTET": 0,
        "STARTTIME": "2022-10-02 02:22:31+07",
        "STOPTIME": "2022-10-02 07:08:21+07",
        "TERMINATECAUSE": null,
        "TOTALUSAGE": 0,
        "USAGETIME": 17150,
        "STATUSKONEKSI": "Stop"
    },
    {
        "USERNAME": "1234567890@telkom.net",
        "CLID": "GPON02-D4-SOP-4 pon 0/4/4/35:2424",
        "FRAMEIPV6ADDRESS": "fd00:448a:402e:1279::/64",
        "FRAMEIPADDRESS": "10.45.148.228",
        "INPUT_OKTET": 1153061700,
        "OUTPUT_OKTET": 24036882428,
        "STARTTIME": "2022-09-30 21:32:59+07",
        "STOPTIME": "2022-10-02 02:22:30+07",
        "TERMINATECAUSE": "Lost-Carrier",
        "TOTALUSAGE": 25189944128,
        "USAGETIME": 103771000,
        "STATUSKONEKSI": "Stop"
    }
]
```
dan untuk URL API mengunakan format sebagai berikut
```
http://[Host]:[Port]/predict
```
dan request method yang digunakan adalah **GET** 
API akan mengembalikan variabel Percentage dan Predict Description beserta valuenya dengan tipe data JSON.

## Hasil Retun API
```
[
    {
        "id": 1,
        "desc": "20-30 hari kebelakang",
        "gangguan": 137003,
        "low_usg": 0,
        "med_usg": 585037,
        "high_usg": 231304
    },
    {
        "id": 2,
        "desc": "10-20 hari kebelakang",
        "gangguan": 6010,
        "low_usg": 0,
        "med_usg": 274831,
        "high_usg": 632136
    },
    {
        "id": 3,
        "desc": "0-10 hari kebelakang",
        "gangguan": 335805,
        "low_usg": 0,
        "med_usg": 323941,
        "high_usg": 264183
    }
]
```
## Contoh mengunakan POSTMAN
![image](/Images/Contoh_Postman.png)
