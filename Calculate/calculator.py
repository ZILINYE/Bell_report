import pandas as pd

#from sqlalchemy import create_engine


def Main(time, phone_code, *argv):
    i = 1
    time_list = time['week_day']
    time_length = len(time_list) / 4
    total = pd.DataFrame()
    # define time range
    while i <= time_length:
        start_hh = time_list[4 * i - 4]
        start_mm = time_list[4 * i - 3]
        end_hh = time_list[4 * i - 2]
        end_mm = time_list[4 * i - 1]
        data_list = list()
        # loop Weekday, Sat and Sun data
        # arg : the list combine all time range for one data(weekday or sat or sun)
        a = 1
        for arg in argv:

            # arg is the single dataframe for the specific
            new1 = pd.DataFrame()
            # arg[i -1] : dataframe for current period
            data = arg[i - 1]
            data_all = data.groupby(['Branch']).count().drop(['start_hh', 'start_mm', 'Missed call'],
                                                             axis=1).fillna(value=0)
            data_missed = data[data['Missed call'] == 'Yes'].groupby(['Branch']).count().drop(
                ['start_hh', 'start_mm', 'Missed call'], axis=1)
            data_missed = pd.merge(data_missed, phone_code, on='Branch', how='right').drop(['Phone number'],
                                                                                           axis=1).set_index(
                ['Branch']).fillna(value=0)
            new1[str(a)+'Missed call'] = data_missed['Receiving number']
            new1[str(a)+'All Call'] = data_all['Receiving number']
            new1[str(a)+'Missed%'] = new1[str(a)+'Missed call'] / new1[str(a)+'All Call']
            new1[str(a)+'Missed%'] = new1[str(a)+'Missed%'].map(lambda n: '{:.2%}'.format(n))
            data_list.append(new1)
            a+=1

        new = pd.concat([data_list[0], data_list[1], data_list[2]], axis=1, sort=False)
        new = new.fillna(value=0).replace('nan%', '0%')
        new['Time Range'] = str(start_hh) + ':' + str(start_mm) + '~' + str(end_hh) + ':' + str(end_mm)
        total = total.append(new)

        i += 1

    total = total.set_index(['Time Range'], append=True).sort_index(sort_remaining=False)
    return total
