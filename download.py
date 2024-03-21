import requests
from bs4 import BeautifulSoup
import hashlib
import os
import csv

url = "https://mzh.moegirl.org.cn/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2"

visited = set()


def clean_text(text):
    cleaned_text = " ".join(text.split())
    return cleaned_text


def download(url):
    if url in visited:
        return
    visited.add(url)
    number = 0
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    with open("output.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        cleaned_soup = BeautifulSoup(str(soup), "html.parser")
        cleaned_text = clean_text(cleaned_soup.get_text())
        writer.writerow([cleaned_text])


download(url)
