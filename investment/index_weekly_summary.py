# encoding: utf-8

"""
@version: 1.7.2
@author: jensen.lau
@license: Apache Licence 
@contact: swordsman.liu@gmail.com
@file: index_weekly_summary.py
@time: 17-6-25 下午4:10
"""
import tushare as ts
import datetime
import requests
from bs4 import BeautifulSoup


def get_last_week():
    """
    get the monday and friday of last week
    :return: 
    """
    now = datetime.datetime.now()
    week_day = now.weekday()
    monday = now + datetime.timedelta(days=-week_day)
    friday = monday + datetime.timedelta(days=4)
    return str(monday)[0:10], str(friday)[0:10]


class IndexWeeklyReport(object):
    """
    A class represents the weekly statistics for main market index, 
    including start index, end index, change rate, average pb, average pe and total fair value  
    sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板
    """
    def __init__(self, code, start_date, end_date):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.open = 0.0
        self.close = 0.0
        self.low = 0.0
        self.high = 0.0
        self.p_change = 0.0
        self.pb = 0.0
        self.pe = 0.0
        self.fair_value = 0.0

    def __str__(self):
        return "%s open %.2f, close %.2f, high %.2f, low %.2f, change percentage is %.2f" % \
               (self.code, self.open, self.close, self.high, self.low, self.p_change)

    def get_report(self):
        """
        Retrieve information
        :return: self 
        """
        # TODO check if the result has been saved, if True load it from file instead of calling Tushare API.
        hist_data = ts.get_hist_data(code=self.code, ktype="W", start=self.start_date, end=self.end_date)
        self.open = hist_data['open']  # 开盘价
        self.close = hist_data['close']
        self.low = hist_data['low']
        self.high = hist_data['high']
        self.p_change = hist_data['p_change']
        # get average pb/pe TODO

        # get fair value for sh/sz TODO
        if self.code == 'sh' or self.code == 'sz':
            pass

        return self

    def _get_sz_market_info(self):
        """
        获取深圳市场的总市值和平均市盈率
        :return: 
        """
        url = "http://www.szse.cn/main/marketdata/tjsj/jbzb/"


    def persist(self):
        """
        save the report result in a file.
        :return: True or False 
        """
        pass


if __name__ == '__main__':
    codes = ["sh", "sz", "cyb", "hs300", "sz50", "zxb"]
    monday, friday = get_last_week()

    for code in codes:
        index_report = IndexWeeklyReport(code, monday, friday)
        index_report.get_report()
        print str(index_report)



