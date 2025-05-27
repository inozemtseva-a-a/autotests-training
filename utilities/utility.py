import softest
import csv


class Utils(softest.TestCase):
    def read_data_from_csv(filename):
        #create an empty list
        datalist = []

        #Open CSV file
        csvdata = open(filename,"r")

        #create CSV reader
        reader = csv.reader(csvdata)

        #skip header (1-st row)
        next(reader)

        #Add csv rows to list
        for rows in reader:
            datalist.append(rows)
        return datalist