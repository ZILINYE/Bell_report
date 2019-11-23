class processor:
    def __init__(self, original_data, file):
        self.original_data = original_data
        self.time = file

    def controller(self):
        # loading Time range

        weekday_data = self.original_data[self.original_data['weekday'] == 'Weekdays']
        sat_data = self.original_data[self.original_data['weekday'] == 'Saturday']
        sun_data = self.original_data[self.original_data['weekday'] == 'Sunday']

        # Get All Valid Weekday data with valid time range but no branch yet
        weekday_final = processor.filter(weekday_data, self.time['week_day'])
        sat_final = processor.filter(sat_data, self.time['week_end'])
        sun_final = processor.filter(sun_data, self.time['week_end'])

        return weekday_final, sat_final, sun_final

    def filter(f_arg, time):

        data_list = list()

        range_num = int(len(time) / 4)
        i = 1

        while i <= range_num:
            start_hh = time[4 * i - 4]
            start_mm = time[4 * i - 3]
            end_hh = time[4 * i - 2]
            end_mm = time[4 * i - 1]

            # determine if is not at same day
            if start_hh < end_hh:
                valid = f_arg[
                    (((f_arg['start_hh'].astype(int)) > start_hh) & ((f_arg['start_hh'].astype(int)) < end_hh)) | (
                                ((f_arg['start_hh'].astype(int)) == start_hh) & (
                        ((f_arg['start_mm'].astype(int)) >= start_mm))) | (
                                ((f_arg['start_hh'].astype(int)) == end_hh) & (
                        ((f_arg['start_mm'].astype(int)) <= end_mm)))]
            # determine if within an hour
            elif start_hh == end_hh:
                valid = f_arg[(((f_arg['start_hh'].astype(int)) == start_hh)&(((f_arg['start_mm'].astype(int)) >= start_mm))&((f_arg['start_mm'].astype(int)) <= end_mm))]

            # determine if is not at same day
            else:

                valid = f_arg[
                    (((f_arg['start_hh'].astype(int)) > start_hh) | ((f_arg['start_hh'].astype(int)) < end_hh)) | (
                                ((f_arg['start_hh'].astype(int)) == start_hh) & (
                        ((f_arg['start_mm'].astype(int)) >= start_mm))) | (
                                ((f_arg['start_hh'].astype(int)) == end_hh) & (
                        ((f_arg['start_mm'].astype(int)) <= end_mm)))]

            i += 1
            data_list.append(valid)
        return data_list
