import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
def import_db(df,date_time):

    engine = create_engine("mysql://kkkye201_zilinye:YZLMM52476@108.167.156.159/kkkye201_python")
    con = engine.connect()
    df= df.droplevel(level=1)
    df['Branch'] = df.index
    df['date_time'] = date_time
    df = df.reset_index(drop=True)
    df.to_sql(name='phone_report', con=engine,if_exists='append',index=False)

