import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

email= "xxx@gmail.com"
password= "XXXXXXX"
target_price = 500

url="https://www.amazon.co.uk/ASUS-VivoBook-X515EA-i5-1135G7-Keyboard/dp/B09F6LCV9N/ref=sr_1_34_sspa?crid=3RXO3R42FODVV&keywords=laptop&qid=1654425811"
user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30"


headers = {
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8",
    "User-Agent": user_agent
}

response = requests.get(url, headers=headers)
data = response.text
soup = BeautifulSoup(data, "lxml")

product_tag = soup.find(name="span", id="productTitle")
product_title= product_tag.getText().strip()

price_tag = soup.find(name="span", class_="a-offscreen")
price= float(price_tag.getText().split("£")[1]) #this removes the £ sign and prints only the price
print(price)

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs="abc@yahoo.com",
                                    msg= f"subject:Amazon Deal\n\n{product_title}is now {price}\nLink: {url}")