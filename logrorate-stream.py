import time
from datetime import datetime, timedelta
import operator
import os

""" Declare variable """
logs = '/Users/dimzrio/PycharmProjects/rotate-streaming/mysql-slowtest.log'
timer = 1 # in minutes

""" Open stream to file """
steam = open(logs, mode='r', buffering=1, encoding=None,
			 errors=None, newline=None, closefd=True)

""" Read buffer from stream """
while True:
	rotate_schedule = datetime.now() + timedelta(minutes=timer)
	ext = rotate_schedule.strftime('%Y-%m-%d_%H%M')
	filename = '{0}-{1}'.format(logs, ext)
	rotate_file = open(filename,'w')
	while True:
		time_now = datetime.now()
		if operator.__le__(time_now, rotate_schedule):
			content = steam.read()
			if content is not None:
				rotate_file.write(content)
			time.sleep(0.5)
		else:
			break
	rotate_file.close()

	""" Remove if file is empty """
	os.remove(filename) if os.stat(filename).st_size == 0 else print('[+] Rotate successfully..!!!')