import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
element = soup.find(class_="a-price-whole")
element = element.text+soup.find(class_="a-price-fraction").text
title = soup.find(id="productTitle").get_text().strip()


price_as_floating=float(element)




if(price_as_floating<=100.00):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="helloarham596@gmail.com",
            msg=f"subject:price drop!! \n\nThe product {title} is now {price_as_floating} link: {url}".encode("utf-8")
        )