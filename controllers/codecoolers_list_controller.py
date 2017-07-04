import os.path
import csv 

def read_codecoolers_list_csv():
    with open (os.path.dirname(__file__) + '../csv_databases/codecoolers_list.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        
        codecoolers_list = []

        for line in reader:
            codecoolers_list.append(line)

    return (codecoolers_list)
    
read_codecoolers_list_csv()