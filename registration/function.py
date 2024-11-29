from BeemAfrica import Authorize, SMS
import base64
import requests

access = '9c3a95f03b8d081b'
secret = 'ODNjZmQzZDQyZmYwZjg3NzAzZGY1YjY2NTViZDE4Y2Y0OTExYmRmNjUwZTg2YjlkZjMxMzQ1Yzk2MTExNmM0OQ'

def send_sms_to_student(msg, phone):
    Authorize(access, secret)
    SMS.send_sms(
        msg,
        phone,
        sender_id='INFO'
    )


def check_balance():
    username = access
    password = secret
    url = 'https://apisms.beem.africa/public/v1/vendors/balance'

    # Set up the headers with Basic Authentication
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8'),
        'Content-Type': 'application/json'
    }

    # Make the GET request
    try:
        response = requests.get(url, headers=headers, verify=True)
        response.raise_for_status()  # Check for errors
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
