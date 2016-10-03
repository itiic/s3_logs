#!/usr/bin/env python

import os

dir_logs = '{{DIR}}'

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

size = get_size(dir_logs)

if size > 576716800:	# 550 MB
	# print the oldest log
	print dir_logs + '/' + min(os.listdir(dir_logs), key=lambda p: os.path.getctime(os.path.join(dir_logs, p)))


