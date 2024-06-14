import csv

with open("../files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("enter a city: ")
# print(data)
for row in data[1:]:
    if row[0] == city:
        print(f"{row[0]} : {row[1]}")
