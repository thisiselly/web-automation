import pyodbc

from utils.logs_util import logger

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-DECQQQS;"
    "DATABASE=HY_Database;" 
    "Trusted_Connection=yes;"
)

class SqlServerDB:
    def __init__(self):
        self.connection = pyodbc.connect(conn_str)
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql):
        try:
            logger.info(f"execute sql：{sql}")
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            logger.info(f"execute sql fail：{sql}")

    def insert_sql(self, sql, params):
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
        except Exception as e:
            logger.info(f"execute sql fail：{e}")

    def select_db_all(self, sql):
        logger.info(f"execute sql command: {sql}")
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()

# if __name__ == '__main__':
#     sqldb = SqlServerDB()
#     sql = 'select * from hy_course'
#     print(sqldb.select_db_all(sql))