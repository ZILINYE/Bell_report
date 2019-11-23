import datetime

def Main(phone_code, original):
    vailid_data = phone_code.merge(original, left_on='Phone number',
                                   right_on='Receiving number')
    # Drop no-need data
    vailid_data = vailid_data.drop(
        ['Row', 'Caller', 'Call type', 'Authorization code', 'Long distance carrier', 'Internal/External',
         'Group name', 'End time', 'Call duration', 'Calling/Receiving', 'Department', 'Call transfer', 'Call park',
         'Call pick-up', 'Redirected Call'], axis=1)
    # time format
    vailid_data['start_yy'] = vailid_data.apply(lambda row: row['Start time'][0:4], axis=1)
    vailid_data['start_mo'] = vailid_data.apply(
        lambda row: int(str(datetime.datetime.strptime(row['Start time'][5:8], '%b'))[5:7]), axis=1)
    vailid_data['start_dd'] = vailid_data.apply(lambda row: row['Start time'][9:11], axis=1)
    vailid_data['start_hh'] = vailid_data.apply(lambda row: row['Start time'][12:14], axis=1)
    vailid_data['start_mm'] = vailid_data.apply(lambda row: row['Start time'][15:17], axis=1)
    vailid_data['weekday'] = vailid_data.apply(
        lambda row: int(datetime.date(int(row['start_yy']), int(row['start_mo']), int(row['start_dd'])).weekday()),
        axis=1)
    # determine weekday for each phone call record
    vailid_data['weekday'] = vailid_data['weekday'].replace([0, 1, 2, 3, 4], 'Weekdays')
    vailid_data['weekday'] = vailid_data['weekday'].replace([5], 'Saturday')
    vailid_data['weekday'] = vailid_data['weekday'].replace([6], 'Sunday')
    vailid_data = vailid_data.drop(['Start time', 'Phone number', 'start_yy', 'start_mo', 'start_dd'],
                                   axis=1).fillna(value='No')
    return vailid_data
