#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import datetime
import numpy as np
from matplotlib.dates import (YEARLY, MONTHLY, DateFormatter, rrulewrapper, RRuleLocator, drange, MonthLocator, DayLocator, AutoDateFormatter, AutoDateLocator)
#from matplotlib.dates import DateFormatter
#from matplotlib.ticker import FixedLocator
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'figure.autolayout': True})

# Fixing random state for reproducibility
np.random.seed(137482457)

my_file = open("wordcount.txt", "r")
content_list = my_file.readlines()
# print(content_list)

dates=[]
y_values=[]
for i in content_list:
    line = i.split("|")
    dates.append(line[0])
    y_values.append(float(line[1]))

x_values=[datetime.datetime.strptime(d,"%Y-%m-%d %H:%M ").date() for d in dates]
# print(y)
# print(dates)

fig,ax=plt.subplots()
plt.plot_date(x_values, y_values, linestyle='solid', marker='x')

plt.grid(True)
plt.gcf().autofmt_xdate()

plt.title("Thesis Word Count", fontsize=20)
plt.xlabel("Date", fontsize=15)
plt.ylabel("Word Count", fontsize=15)
plt.xticks(rotation=80)
plt.savefig("wordcount.png")
plt.show()
plt.close()
