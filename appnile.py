import os
import csv

os.system("echo Pulling from postgres...")
os.system("heroku pg:psql postgresql-dimensional-74388 --app appnile --command \"COPY (player) TO STDOUT WITH CSV\" > file.csv")
os.system("echo Done!")

file = open("file.csv")
csvreader = csv.reader(file)

header = next(csvreader)
print(header)

for rows in csvreader:
    print(rows)

file.close()
