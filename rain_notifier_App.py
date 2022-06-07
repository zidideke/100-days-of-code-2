import requests

api_key= "79eb606aec45bc6e9021d48468a3a30e"
MY_LAT =36.144909
MY_LONG = -5.353250
#https://api.openweathermap.org/data/2.5/weather?lat=36.200146&lon=-95.98282&appid=79eb606aec45bc6e9021d48468a3a30e
7
#https://api.openweathermap.org/data/2.5/onecall?lat=36.200146&lon=-95.987282&exclude={part}&appid=79eb606aec45bc6e9021d48468a3a30e
#https://api.openweathermap.org/data/2.5/onecall?lat=36.200146&lon=-95.987282&appid=79eb606aec45bc6e9021d48468a3a30e

parameter ={
        "lat":MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "exclude": "current,minutely,daily"

}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
#print(response.status_code)

weather_data =response.json()
#print(data["hourly"][0]["weather"][0]["id"]) #prints the weather ID for the 0th hour

weather_slice=weather_data["hourly"][:12]


will_rain=False

for hour_data in weather_slice:
    condition_code= hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)



#https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}