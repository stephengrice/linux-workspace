#!/usr/bin/env python3

import csv, os

WORKING_DIRECTORY_NAME = 'wkdir'

if __name__ == "__main__":
	with open('repos.csv') as file:
		csv_data = csv.reader(file, delimiter=',')
		for row in csv_data:
			remote_path = row[1]
			local_path = row[0]
			if os.path.exists('%s/%s' % (WORKING_DIRECTORY_NAME, local_path)):
				print('Already exists: %s' % local_path)
			else:
				print('Cloning repository...')
				command = 'git clone %s wkdir/%s' % (remote_path, local_path)
				print(command)
				os.system(command)
