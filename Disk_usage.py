from datetime import datetime
import csv,os


FILE_NAME = 'test'
fname = datetime.now().strftime(FILE_NAME + '_%Y_%m_%d_%H_%M_%S' + '.csv')

def create_file(a):
    with open(fname,'a',newline='') as file:
      csv_file = csv.writer(file)
      csv_file.writerow(a)


def get_value():
    try:
        du = os.popen("df -k").readlines()
        # print(du)
        for line in du:
            # print(i)
            line = line.replace('"', '').strip()
            list_1 = line.split()
            create_file(list_1)

    except Exception as e:
            print(str(e))
get_value()
