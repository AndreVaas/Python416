import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    row = requests.get(url)
    return row.text


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for el in elements:
        name = el.find("h3").text
        url = el.find("h3").find("a").get("href")
        price = el.find("div", class_="product_price").text.strip()

        data = {
            "name": name,
            "url": url,
            "product_price": price,

        }
        write_csv(data)


def write_csv(data):
    with open("news.csv", "a", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data["name"], data["url"], data["product_price"]))


def main():
    url = f"https://books.toscrape.com/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()

#