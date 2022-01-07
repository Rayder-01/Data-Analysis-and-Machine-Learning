import csv

fn = 'yourCSV.csv'

with open(fn, 'w', newline= '') as csvFile:

    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['姓名','年齡','電話','地址'])
    csvWriter.writerow(['大熊','18','1911-123-123','台北市'])
    csvWriter.writerow(['小熊','16','1911-333-333','台中市'])   