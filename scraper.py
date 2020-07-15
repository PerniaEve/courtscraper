import requests
from datetime import datetime  
from datetime import timedelta
import json
import time
import random
auth_key = "51001BB6E39CCC3B3DD61CF88B591253F006124F0BF99835FF0DB8755F7C6715"
s = requests.Session()

def initial_login():
    print("initial_login")
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '163',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'www.clericusmagnus.com:8443',
        'Origin': 'https://www.clericusmagnus.com:8443',
        'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }

    form_data = {
        'SRCHFMT1.BTNEXIT': '0',
        'SRCHFMT1.DOMNAM': 'www.clericusmagnus.com',
        'SRCHFMT1.HOSTNM': 'www.clericusmagnus.com:8443',
        'SRCHFMT1.BTNSCHED': '1',
        'SRCHFMT1.NAMESRCH': '0',
        'SRCHFMT1.CASESRCH': '0'
    }

    url = f'https://www.clericusmagnus.com:8443/profoundui/PUI0001200.pgm/{auth_key}'
    s.headers.update(headers)
    s.post(url,data=form_data)


def login1():
    print("Login 1")
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '243',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'www.clericusmagnus.com:8443',
        'Origin': 'https://www.clericusmagnus.com:8443',
        'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    form_data = {
        'DSP71003.NXTYPE': 'I',
        'DSP71003.BTNDOCKET': '0',
        'DSP71003.INQEVT': '',
        'DSP71003.INQEV2': '',
        'DSP71003.JUDNAM': '',
        'DSP71003.SCHRS': '00',
        'DSP71003.SCMIN': '00',
        'DSP71003.AMPM': '',
        'DSP71003.INQTYP': '',
        'DSP71003.INQTY2': '',
        'DSP71003.BTNRETURN': '1',
        'DSP71003.CURLIN': '0',
        'toprrn.3': '1',
        'DSP71003.BTNBACK': '0'
    }

    url = f'https://www.clericusmagnus.com:8443/profoundui/PUI0001200.pgm/{auth_key}'
    s.headers.update(headers)
    s.post(url,data=form_data)


def login2():
    print("Login 2")
    form_data = {
        'AUTH': auth_key,
        'q': 'dspf.SchTime',
        'datfmt': '1',
        'datsep': '1',
        'timfmt': '1',
        'timsep': '6',
        'UTF8': 'Y'
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '127',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'www.clericusmagnus.com:8443',
        'Origin': 'https://www.clericusmagnus.com:8443',
        'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }

    url = 'https://www.clericusmagnus.com:8443/profoundui/PUI0009103.PGM'
    s.headers.update(headers)
    s.post(url,data=form_data)
    return

def login3():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'www.clericusmagnus.com:8443',
        'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
    s.headers.update(headers)
    
    print("Login 3a")
    chwho = 6
    url = f"https://www.clericusmagnus.com:8443/profoundui/universal/WHODD"
    url_data = {
       "PARMIN": "CHWHO%20%20%20%20%20%20%200",
       "AUTH": auth_key 
    }
    payload_str = "&".join("%s=%s" % (k,v) for k,v in url_data.items())

    
    r = s.get(url, params=payload_str)
    print(r.url)
    print(r.text)

    print("Login 3b")
    url_data = {
       "PARMIN": "CHWHO%20%20%20%20%20%20%206",
       "AUTH": auth_key 
    }
    payload_str = "&".join("%s=%s" % (k,v) for k,v in url_data.items())
    r = s.get(url, params=payload_str)
    print(r.text)
    return



def getData(start_date, end_date):
    referrer = 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3'
    url = f'https://www.clericusmagnus.com:8443/profoundui/PUI0001200.pgm/{auth_key}'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '499',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'www.clericusmagnus.com:8443',
        'Origin': 'https://www.clericusmagnus.com:8443',
        'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
    start = start_date.strftime("%m%d%Y")
    end = end_date.strftime("%m%d%Y")
    post_data = {
        "DSP71000.BTNHELP": 0,
        "DSP71000.SCDATE": start,
        "DSP71000.NEXTD": 5,
        "DSP71000.SAVJUD": "",
        "DSP71000.TODATE": end,
        "DSP71000.SCHTIMEZ": "08:00 AM",
        "DSP71000.INQN23X": "",
        "DSP71000.ATTORNEY": "",
        "DSP71000.CROOM": "",
        "DSP71000.INQTY2": "",
        "DSP71000.AMPM": "AM",
        "DSP71000.COURTY": "6",
        "DSP71000.NXTCHG": 0,
        "DSP71000.JUDGE": "",
        "DSP71000.INQTYP": "",
        "DSP71000.INQEVT": "",
        "DSP71000.ROOM": "",
        "DSP71000.NXTYPE": "I",
        "DSP71000.SCHRS": "08",
        "DSP71000.CODE": "I",
        "DSP71000.INQEV2": "",
        "DSP71000.SCMIN": "00",
        "DSP71000.INQN23": "",
        "DSP71000.BTNRETURN": 0,
        "DSP71000.CURRCD": "DSP71000",
        "DSP71000.CURFLD": "INQN23X",
        "DSP71000.CURPOS": 1,
        "row": 4,
        "column": 54,
        "DSP71000.BTNBACK": 0
    }

    s.headers.update(headers)

    try:
        print(f"Attempting {start} - {end}")
        r = s.post(url, data=post_data, headers=headers)
        response = r.json()
        response_data = response["layers"][0]["formats"][0]["subfiles"]
        keys = response_data.keys()
        for key in keys:
            court_data = response_data[key]["data"]
            fname = start_date.strftime("%Y%m%d") + "_" + end_date.strftime("%Y%m%d") + ".json"
            f = open(fname, 'w')
            f.write(json.dumps(court_data))
            f.close()
    except:
        print(f"Attempted {start} - {end} but it failed. Session expired?")
        exit()
    print(f"Processed {start} - {end}")
    print("--------------------------------")


start = datetime(2020, 6, 25)
end = start + timedelta(days=4)
final_date = datetime(2022, 1, 1)
initial_login()

while end.date() <= final_date.date():
    login1()
    login2()
    login3()
    getData(start, end)
    start = end + timedelta(days=1)
    end = start + timedelta(days=6)
    time.sleep(10)

"""
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'www.clericusmagnus.com:8443',
    'Referer': 'https://www.clericusmagnus.com:8443/profoundui/start?pgm=EDOCS/WDI040CL&p1=%20CH&l1=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
s.headers.update(headers)
print("Login 3a")
chwho = 6
url = f"https://www.google.com"
url_data = {
    "PARMIN": "CHWHO       6",
    "AUTH": auth_key 
}
r = s.get(url, params=url_data)
print(r.url)
#print(r.text)
"""