import requests
from bs4 import BeautifulSoup
import smtplib

import os
from dotenv import load_dotenv
load_dotenv()


url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
element = soup.find(class_="a-price-whole")
element = element.text+soup.find(class_="a-price-fraction").text
title = soup.find(id="productTitle").get_text().strip()


price_as_floating=float(element)

my_mail = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")


if(price_as_floating<=100.00):
    message = f"""Subject: Price Drop Alert!
    The product:
    {title}
    is now available for ${price_as_floating}
    Buy here:
    {url}
    """

    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="cse.23bcse65@silicon.ac.in",
            msg=message.encode("utf-8")
        )