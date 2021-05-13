import requests
from datetime import datetime
PINCODE='390020'
DATE1='13-05-21'
def  create_session_info(center,session):
    return{"name":center["name"],
           "date": session["date"],
           "capacity": session["capacity"],
           "age_limit": session["min_age_limit"]
           }


def get_sessions(data):
    for center in data["centers"]:
        for session in center["sessions"]:
          yield create_session_info(center, session)


def is_available(session):
    return session["capacity"]>0

def is_eighteenplus(session):
    return session["age_limit"]==18

def get_for_seven_days(start_date):
  url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
  params={"pincode":390020,"date":start_date.strftime("%d-%m-%y")}
  resp=requests.get(url, params)
  data=resp.json()
  return [session for session in get_sessions(data) if is_eighteenplus(session) and is_available(session)]

def create_output(session_info):
    return f"({session_info['date']}-{session_info['name']}{session_info['date']})"
    content="\n".join([create_output(session_info) for session_info in get_for_seven_days(datetime.today())])
    if not content:
      print("No availablity")
    else:
       print(content)
        