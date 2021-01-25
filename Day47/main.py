import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.in/LG-Inverter-Fully-Automatic-FHM1006ADW-Technology/dp/B08CPQVLZT/ref=lp_22489506031_1_3"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find("span",class_="a-size-base a-color-price").get_text()
print(price)
# price_without_currency = price.split("₹")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)

# title = soup.find(id="productTitle").get_text().strip()
# print(title)

# BUY_PRICE = 200

# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"

#     with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
#         connection.starttls()
#         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
#         connection.sendmail(
#             from_addr=YOUR_EMAIL,
#             to_addrs=YOUR_EMAIL,
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
#         )
