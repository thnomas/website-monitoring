import os
import requests
import datetime
import smtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

url = "https://movies.thnomas.com/"
now = datetime.datetime.now()

def send_email(email_address: str , email_password: str) -> None:    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = f'Website Down: {url}'
        body = f'Non 200 response code ({r.status_code}) - there is an issue with your website {url}.\n\nBest of luck with that.\n\nThomas'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def check_status(r):
    if r.status_code == 200:
        print(f"{now}: OK - {r.status_code}")
    else:
        print(f"Non 200 response code ({r.status_code}) - there is an issue with the website.")
        send_email(EMAIL_ADDRESS, EMAIL_PASSWORD)

try:
    r = requests.get(url)
    check_status(r)
except requests.exceptions.RequestException as e:
    print(f"There was an issue getting a response: {e}")

