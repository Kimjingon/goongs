import time

import streamlit as st
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from client.mysql_client import MysqlClient


def get_car_cnt_data():
    url = "https://kosis.kr/visual/nsportalStats/detailContents.do?statJipyoId=3707&listId=L&vStatJipyoId=5222"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="bd_lst_tbl")

    data = []
    tr = table.find("tbody").find("tr")
    for td in tr.find_all("td")[1:]:
        key = td["data-cell-header"].replace(".", "-")
        value = td.get_text(strip=True).replace(",", "")
        data.append((key, int(value)))

    return data



if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)

    columns = ["year_month_id", "cnt"]
    table = "car_cnt_info"

    db = MysqlClient(
        host=st.secrets["db"]["host"],
        user=st.secrets["db"]["user"],
        password=st.secrets["db"]["password"],
        database=st.secrets["db"]["database"],
    )
    car_cnt_data = get_car_cnt_data()
    db.insert_data(data=car_cnt_data, columns=columns, table=table)
    db.close()
    driver.quit()
