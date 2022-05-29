# NoFap dates.

import calendar
import datetime as DT


class NoFapDates(object):
    """
    This class creates dates and writes them to a file.
    """
    def __init__(self, start_date, in_=None, how_many=1):
        self.start_date = start_date
        self.end_date = None
        if calendar.isleap(self.start_date.year):
            self.all_days = 366
        else:
            self.all_days = 365
        self.in_ = in_.lower()
        if self.in_ == 'w':
            self.interval = 6
        elif self.in_ == 'd':
            self.interval = 0
        self.how_many = how_many
        self.divisions = self.all_days // (self.interval + 1)

    def get_dates(self):
        """
        This method fetches the dates in a list object.
        """
        date_list = list()
        for this_many in range(self.how_many):
            date_list.append('Year --> ' + str(this_many+1) + '\n')
            for nfd in range(self.divisions):
                self.end_date = self.start_date + DT.timedelta(days=self.interval)
                start_date_str = self.start_date.strftime('%Y/%m/%d')
                end_date_str = self.end_date.strftime('%Y/%m/%d')
                nofap_date = start_date_str + ' - ' + end_date_str + '\n'
                date_list.append(nofap_date)
                self.start_date = self.end_date + DT.timedelta(days=1)
        return date_list

    def write_dates_to_file(self):
        """
        This methods writes all the dates to a file.
        """
        with open(file='nofap_dates.txt', mode='w') as nf_date_file:
            nf_date_file.writelines(self.get_dates())
        print('Dates are published!')
        return None


if __name__ == '__main__':
    start_date = DT.datetime(2020, 10, 3)
    nofapdates = NoFapDates(start_date=start_date, in_='w', how_many=5)
    nofapdates.write_dates_to_file()


# EOF 