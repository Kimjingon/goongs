import time

import streamlit as st
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from mysql_client import MysqlClient

if __name__ == "__main__":

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    url = "https://kosis.kr/visual/nsportalStats/detailContents.do?statJipyoId=3707&listId=L&vStatJipyoId=5222"
    driver.get(url)

    time.sleep(2)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="bd_lst_tbl")

    rows = []
    tr = table.find("tbody").find("tr")
    for td in tr.find_all("td")[1:]:
        key = td["data-cell-header"].replace(".", "-")
        value = td.get_text(strip=True).replace(",", "")
        rows.append((key, int(value)))
    driver.quit()

    db = MysqlClient(
        host=st.secrets["db"]["host"],
        user=st.secrets["db"]["user"],
        password=st.secrets["db"]["password"],
        database=st.secrets["db"]["database"],
    )
    columns = ["year_month_id", "cnt"]
    table = "car_cnt_info"
    db.insert_data(data=rows, columns=columns, table=table)
    db.close()
