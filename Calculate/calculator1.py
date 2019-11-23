import pandas as pd

def Main(time, phone_code, *argv):
    # define time range
    data_list = list()
    week_list = ['Mon~Fri', 'Sat', 'Sun']
    total = pd.DataFrame()
    y = 0

    for arg in argv:


        time_list = time['week_day']
        time_length = len(time_list) / 4
        i = 1
        data_list1 = []
        while i <= time_length:
            new1 = pd.DataFrame()
            # arg is the single dataframe for the specific

            # arg[i -1] : dataframe for current period
            data = arg[i - 1]

            data_all = data.groupby(['Branch']).count().drop(['start_hh', 'start_mm', 'weekday', 'Missed call'],
                                                             axis=1).fillna(value=0)

            data_missed = data[data['Missed call'] == 'Yes'].groupby(['Branch']).count().drop(
                ['start_hh', 'start_mm', 'weekday', 'Missed call'], axis=1)

            data_missed = pd.merge(data_missed, phone_code, on='Branch', how='right').drop(['Phone number'],
                                                                                           axis=1).set_index(
                ['Branch']).fillna(value=0)

            new1['Missed call'] = data_missed['Receiving number']
            new1['All Call'] = data_all['Receiving number']
            data_list1.append(new1)
            i += 1
            # append all period dataframe to list
        new2 = pd.concat([df for df in data_list1], axis=1, sort=True)
        new2['week'] = week_list[y]
        data_list.append(new2)
        y += 1
    total = total.append([df for df in data_list])
    total = total.reset_index().set_index(['index', 'week'], append=False).sort_index()
    total = total.fillna(value=0).replace('nan%', '0%')
    return total
