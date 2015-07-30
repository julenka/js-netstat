#!/usr/bin/env python
# coding=utf-8
""" Draw upload speed curves
"""
__author__ = 'julenka'

import csv
import datetime
import matplotlib.pyplot as plt
import numpy as np

minutes_to_plot = 480 # plot 8 hours of data

def parse_csv(csv_path):
    x_values = []
    y_values = []
    start_time = None
    with open(csv_path) as f:
        reader = csv.reader(f)
        for line in reader:
            date = datetime.datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
            obytes = int(line[1])
            if not start_time:
                start_time = date
            t = (date - start_time).total_seconds() / 60.
            x_values.append(t)
            y_values.append(obytes / float(1e6)) # divide by 1e6 for Mb
    return np.array(x_values[:minutes_to_plot]), np.array(y_values[:minutes_to_plot])



x1, y1 = parse_csv("obytes-1Mbps-2015_07_28.csv")
dy1_dx1 = y1[1:] - y1[:-1]

x2, y2 = parse_csv("obytes-no_limit-2015_07_29.csv")
dy2_dx2 = y2[1:] - y2[:-1]

plt.subplot(1,2,1)
plt.ylabel("output Mb")
plt.xlabel("minutes")

plt.plot(x1, y1, label="limit @ 1Mbps")
plt.plot(x2, y2, label="no limit")
plt.title("Mb uploaded")

plt.subplot(1, 2, 2)
plt.ylabel("output Mbps")
plt.xlabel("minutes")
plt.title("Upload rate")

plt.plot(x1[1:], dy1_dx1 / 60., label="limit @ 1Mbps")
plt.plot(x2[1:], dy2_dx2 / 60., label="no limit")

plt.legend()
plt.show()
