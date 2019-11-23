import pandas as pd
import shutil
from Template import time_list

def Main(code):

    if code == 'all':
        phone_code = pd.read_csv('Template/phone_code/all.csv')
        time_file = time_list.regular
        shutil.copyfile('Template/regular.xlsx', 'Output/report.xlsx')
    elif code == 'FrontDesk':
        phone_code = pd.read_csv('Template/phone_code/FrontDesk.csv')
        time_file = time_list.regular

    elif code == 'BackEnd':
        phone_code = pd.read_csv('Template/phone_code/BackEnd.csv')
        time_file = time_list.regular

    elif code == 'cf':
        phone_code = pd.read_csv('Template/phone_code/cf.csv')
        time_file = time_list.CF

    elif code == 'other':
        phone_code = pd.read_csv('Template/phone_code/other.csv')
        time_file = time_list.other
    else:
        shutil.copyfile('Template/specific.xlsx', 'Output/report.xlsx')
        phone_code = pd.read_csv('Template/phone_code/specific.csv')
        time_file = time_list.specific
        
    phone_code['Phone number'] = phone_code['Phone number'].astype(str)
    return phone_code,time_file

