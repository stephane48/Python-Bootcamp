from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/124.0.0.0 Safari/537.36")
ACCEPT_LANGUAGE = "en-GB,en;q=0.9,en-US;q=0.8,fr;q=0.7"
MY_EMAIL = "xxxx"
MY_PASSWORD = "xxxx"

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}

response = requests.get(URL, headers=headers)
link = response.text

soup = BeautifulSoup(link, "lxml")
product = soup.find(name="span", id="size_name_0_price")
product_price = float(product.getText().split("$")[1])
# print(product_price)

title = soup.find(name="span", id="productTitle")
product_title = title.getText().split("        ")[1]


if product_price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="stephanekamdem09@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{product_title}is now ${product_price}\n{URL}".encode("utf-8")
        )






