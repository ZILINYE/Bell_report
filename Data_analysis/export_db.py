from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import plotly.graph_objects as go
import pandas as pd

def export_db():
    engine = create_engine("mysql://kkkye201_zilinye:YZLMM52476@108.167.156.159/kkkye201_python")
    con = engine.connect()
    data = pd.read_sql("SELECT * FROM phone_report",con)
    list1 = ['RH','CC','MK','NY','UV','SC','DT']
    fig = go.Figure()
    for item in list1:
        newpd = data.loc[data['Branch']==item]
        a=newpd['1Missed call']
        b=newpd['date_time']
        fig = fig.add_trace(go.Scatter(x=b,y=a,mode='lines',name=item))
    fig.show()

export_db()