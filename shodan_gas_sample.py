# File: shodan_gas_sample.py
# Desc: Shodan query for gas inv in AZ. Sends alert via Gmail and Twilio if found.
# Auth: Dakota Kartchner
# Date: 4/19/2025

import shodan
import ezgmail
from twilio.rest import Client

# Shodan Setup
SHODAN_API_KEY = 'YOUR_SHODAN_API_KEY_HERE'
api = shodan.Shodan(SHODAN_API_KEY)
search_query = "'in-tank inventory' state:'AZ'"

# Gmail Setup (Make sure credentials.json and token.json are in the same directory)
ezgmail.init()

# Twilio Setup
account_sid = 'YOUR_TWILIO_ACCOUNT_SID_HERE'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN_HERE'
twilio_from = 'YOUR_TWILIO_PHONE_NUMBER'  # e.g., '+12345678900'
twilio_to = 'YOUR_VERIFIED_PHONE_NUMBER'  # e.g., '+19876543210'
client = Client(account_sid, auth_token)

# Message Preparation
msg = ""
phoenix_found = False

try:
    results = api.search(search_query)
    matches = results.get("matches", [])

    for match in matches:
        data = match.get("data", "No data found")
        msg += data + "\n\n"

        if "Phoenix" in match.get("location", {}).get("city", ""):
            phoenix_found = True

    # Send Email Report
    ezgmail.send(
        'YOUR_EMAIL_ADDRESS',  # e.g., 'youremail@example.com'
        'Internet Gas Gauges in AZ',
        msg
    )

    # SMS confirmation
    client.messages.create(
        body="Internet Gas Gauge in AZ report delivered to email.",
        from_=twilio_from,
        to=twilio_to
    )

    # Alert if Phoenix found
    if phoenix_found:
        client.messages.create(
            body="ALERT: Exposed gas gauge found in Phoenix, AZ!",
            from_=twilio_from,
            to=twilio_to
        )

    print("Search complete. Report emailed.")
    if phoenix_found:
        print("ALERT: Phoenix, AZ gas gauge detected.")

except shodan.APIError as error:
    print(f"Shodan Error: {error}")
except Exception as e:
    print(f"Unexpected error: {e}")