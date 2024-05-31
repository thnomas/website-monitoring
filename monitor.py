import requests
import datetime

url = "https://movies.thnomas.com/"
now = datetime.datetime.now()

def check_status(r):
    if r.status_code == 200:
        print(f"{now}: OK - {r.status_code}")
    else:
        print(f"Non 200 response code ({r.status_code}) - there is an issue with the website.")

try:
    r = requests.get(url)
    check_status(r)
except requests.exceptions.RequestException as e:
    print(f"There was an issue getting a response: {e}")

