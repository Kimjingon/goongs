import streamlit as st
import pandas as pd


def show(db):
    st.title("자동차 등록 현황")
    date_range = db.get_date_range()
    min_date = pd.to_datetime(date_range["min_date"], format="%Y-%m")
    max_date = pd.to_datetime(date_range["max_date"], format="%Y-%m")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input(
            "시작 날짜",
            value=min_date.date(),
            min_value=min_date.date(),
            max_value=max_date.date()
        )
    with col2:
        end_date = st.date_input(
            "종료 날짜",
            value=max_date.date(),
            min_value=min_date.date(),
            max_value=max_date.date()
        )
    data = db.get_car_data(start_date, end_date)
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.line_chart(df.set_index("year_month_id")["cnt"])