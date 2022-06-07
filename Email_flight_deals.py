
import requests

sheet_endpoint="https://api.sheety.co/686865192a864917c5033af7604e2f71/copyOfFlightDeals/sheet2"

print("Welcome to Gladys' Flight Club.\nW find the best flight deals and email you.")
first_name=input("What is your first name? ").title()
last_name=input("What is your last name? ").title()
email=input("What is your email? ").lower()
verify_email=input("Type your email again: ").lower()

if email == verify_email:
  print("You're in the club.")

user_input= {
  "First Name": first_name,
  "Last Name": last_name,
  "Email":verify_email
}

response = requests.post(url=sheet_endpoint, json=user_input)
print(response.status_code)
response.json()