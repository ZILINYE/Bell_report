import pandas as pd
from Template import temp
from Data_process import process
from Calculate import calculator1, calculator
from output import excel
from Data_process import initialize
import time
import glob
from Data_analysis import import_db


def main():
    # select mode (Regular  or Specific)
    mode = int(input("Please enter code : \n1:Regular\n2:Specific\n:"))
    start = time.time()
    # load Original Data File
    print('Loading Original Data File...')
    for file in glob.glob("*.csv"):
        file_path = file

    Original = pd.read_csv(file_path, low_memory=False)
    file_path = list(file_path)
    file_path = file_path[-21:-4]
    date_time = ''
    for a in file_path:
        date_time = date_time + str(a)


    # Initialize Original Data
    all = 'all'
    phone_code, time_file = temp.Main(all)
    original_data = initialize.Main(phone_code, Original)

    # regular Process
    if mode == 1:

        # FrontDesk
        front = 'FrontDesk'
        phone_code, time_file = temp.Main(front)
        front_processor = process.processor(original_data, time_file)
        front_week, front_sat, front_sun = front_processor.controller()
        total_front = calculator.Main(time_file, phone_code, front_week, front_sat, front_sun)
        excel.Main(total_front, front)
        import_db.import_db(total_front, date_time)


        # BackEnd
        back = 'BackEnd'
        phone_code, time_file = temp.Main(back)
        back_processor = process.processor(original_data, time_file)
        back_week, back_sat, back_sun = back_processor.controller()
        total_back = calculator.Main(time_file, phone_code, back_week, back_sat, back_sun)
        excel.Main(total_back, back)

        cf = 'cf'
        phone_code, time_file = temp.Main(cf)
        cf_processor = process.processor(original_data, time_file)
        cf_week, cf_sat, cf_sun = cf_processor.controller()
        total_cf = calculator.Main(time_file, phone_code, cf_week, cf_sat, cf_sun)
        excel.Main(total_cf, cf)
        #
        other = 'other'
        phone_code, time_file = temp.Main(other)
        other_processor = process.processor(original_data, time_file)
        other_week, other_sat, other_sun = other_processor.controller()
        total_other = calculator1.Main(time_file, phone_code, other_week, other_sat, other_sun)
        excel.Other(total_other, time_file, other)
    # specific Process
    else:
        # Loading Template
        specific = 'specific'
        phone_code, time_file = temp.Main(specific)
        # init Process
        processor = process.processor(original_data, time_file)
        sp_week, sp_sat, sp_sun = processor.controller()
        total_sp = calculator1.Main(time_file, phone_code, sp_week, sp_sat, sp_sun)
        excel.Main(total_sp, specific)
    end = time.time()
    print('Total Spend : ' + '{:.2f}'.format(float(end - start))+' s')


main()
