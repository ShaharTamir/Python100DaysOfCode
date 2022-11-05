# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)

    temperatures = []
    for row in data:
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    print(temperatures)

import pandas

data_too = pandas.read_csv("weather_data.csv")
print(data_too) # print data read from csv file.
print(data_too.temp.mean()) # print the average of temp column
