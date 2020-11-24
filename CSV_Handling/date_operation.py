# -*- coding: utf-8 -*-
from datetime import datetime, date
import calendar


class DateOperations:
    def format_date_str(self, date, format_str='%Y-%m-%d'):
        return date.strftime(format_str)

    def get_month_day_range(self, date, report_date, is_format=False, format_str='%Y-%m-%d', ):
        if date:
            first_day = report_date and (datetime.strptime(report_date, '%Y-%m-%d').date())
            last_day = date.replace(day=calendar.monthrange(date.year, date.month)[1])
            if not is_format:
                return first_day, last_day
            else:
                return first_day.strftime(format_str), last_day.strftime(format_str)
        return ()

    def get_month_day_range_move(self, date, is_format=False, format_str='%Y-%m-%d'):
        if date:
            first_day = date.replace(day=1)
            last_day = date.replace(day=calendar.monthrange(date.year, date.month)[1])
            if not is_format:
                return first_day, last_day
            else:
                return first_day.strftime(format_str), last_day.strftime(format_str)
        return ()

    def month_list(self, year=False, stmonth=False):
        months_choices = []
        total_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if not year:
            year = date.today().year
        if stmonth:
            endmonth = stmonth - 1
            stmonth_list = total_months[stmonth - 1:]
            endmonthlist = total_months[:endmonth]
            total_list = stmonth_list + endmonthlist
            for i in total_list:
                nyear = year
                if i >= 1 and i <= endmonth:
                    nyear += 1
                date_st = str(nyear) + '-' + str(i) + '-' + '1'
                months_choices.append((i, datetime.strptime(date_st, '%Y-%m-%d').date()))
        else:
            for i in range(1, 13):
                date_st = str(year) + '-' + str(i) + '-' + '1'
                months_choices.append((i, datetime.strptime(date_st, '%Y-%m-%d').date().strftime('%B')))
        return months_choices

    def get_year_all_months(self, report_date, move_only, fyear=False, fmonth=False):
        if not fyear:
            fyear = date.today().year
        if not fmonth:
            fmonth = date.today().month
        fdate = str(fyear) + '-' + str(fmonth) + '-' + '1'
        date_str = datetime.strptime(fdate, '%Y-%m-%d').date()

        date_dict = []
        # print month_list()
        # print month_list(date_str.year)
        for x in self.month_list(date_str.year, date_str.month):
            # mrange = get_month_day_range(x[1])
            if move_only:
                mrange = self.get_month_day_range_move(x[1], 1)
            else:
                mrange = self.get_month_day_range(x[1], report_date, 1)
            date_dict.append({x[1].month: {'start': mrange[0], 'end': mrange[1]}})
        return date_dict
