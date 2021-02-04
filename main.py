from bs4 import BeautifulSoup
import requests
import smtplib

BUY_PRICE = 450
MY_EMAIL = "your-email"
MY_PASSWORD = "password"
URL = "https://www.amazon.ca/TCL-Dolby-Vision-QLED-Smart/dp/B088517GLM/ref=sr_1_1?dchild=1&keywords=tcl+4k+tv&qid=1609476277&sr=8-1"
headers = {
    "Accept-Language": "en-ca",
    "User-Agent": "xxxx"
}

response = requests.get(URL, headers=headers)
website = response.text

soup = BeautifulSoup(website, "lxml")

price_tag = soup.find(name="span", id="priceblock_ourprice")
price = float(price_tag.getText().split()[1])

title_tag = soup.find(name="span", id="productTitle")
title = title_tag.getText()

if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port="587") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="your-address",
            msg=f"Subject:Amazon price alert\n\nThe price is lower than the $450 CAD, it's time to buy {title}\nThe link is {URL}"
        )





