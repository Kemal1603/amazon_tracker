import requests
from bs4 import BeautifulSoup
import os
import smtplib

header_for_amazon = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,tg;q=0.6"
}

response = requests.get(url="https://www.amazon.com/"
                            "Apple-MacBook-13-inch-256GB-Storage/dp/B08N5N6RSS/ref=sr_1_4?"
                            "dchild=1&keywords=macbook+pro+13+inch+2020&qid=1607598134&sr=8-4", headers=header_for_amazon)
amazon_item_page = response.text
soup = BeautifulSoup(amazon_item_page, "html.parser")
price = int(soup.find('span', id="priceblock_ourprice").getText()[1:6].replace(",", ""))

my_email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

if price < 1000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kemalis5@live.com",
                            msg=(f"Subject: Стоимость Макбука упала!\n\n "
                                 f"'Цена Макбука уже ниже некуда!!! Надо брать!'").encode('utf-8'))
