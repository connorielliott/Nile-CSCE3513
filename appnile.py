import os
import pandas as pd

os.system("echo Pulling from postgres...")
os.system("heroku pg:psql postgresql-dimensional-74388 --app appnile --command \"COPY (SELECT * FROM player) TO STDOUT WITH CSV\" > file.csv")
os.system("echo Done!")

df = pd.read_csv("file.csv")
print(df)
