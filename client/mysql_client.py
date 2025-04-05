import pymysql
from pymysql.err import MySQLError


class MysqlClient:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, data, columns, table):
        try:
            sql = f"""
                 INSERT INTO `{table}` ({', '.join(f'`{col}`' for col in columns)})
                 VALUES ({', '.join(['%s'] * len(columns))})
                """
            self.cursor.executemany(sql, data)
            self.conn.commit()
            return self.cursor.rowcount
        except MySQLError as e:
            print("MySQL 에러 발생 (insert_data):", e)
            return None

    def get_faq_data(self):
        try:
            sql = f"SELECT title, content FROM faq"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except MySQLError as e:
            print("MySQL 에러 발생 (get_data):", e)
            return None

    def get_car_data(self, start_date:str, end_date:str):
        try:
            sql = f"SELECT year_month_id, cnt  FROM car_cnt_info WHERE year_month_id > '{start_date}'" \
                  f" and year_month_id < '{end_date}' ORDER BY year_month_id"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except MySQLError as e:
            print("MySQL 에러 발생 (get_data):", e)
            return None

    def get_date_range(self):
        try:
            sql = "SELECT min(year_month_id) as min_date, max(year_month_id) as max_date FROM car_cnt_info"
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except MySQLError as e:
            print("MySQL 에러 발생 (get_data):", e)
            return None

    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print("연결 종료 중 오류:", e)
