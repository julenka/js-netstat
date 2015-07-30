#!/bin/bash

while :; do python log_netstat.py | tee -a obytes-no_limit_2015_07_29.csv; sleep 60; done