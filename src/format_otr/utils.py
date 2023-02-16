import json
from bs4 import BeautifulSoup


def get_json_from_file(file):
    otr_file_contents = file.read_text()
    otr_json = json.loads(otr_file_contents)
    return otr_json


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_all_timestamps(soup):
    return soup.findAll("span", {"class": "timestamp"})
