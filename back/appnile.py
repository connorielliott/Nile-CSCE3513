import os
import pandas as pd

#os.system("echo Pulling from postgres...")
#os.system("heroku pg:psql postgresql-dimensional-74388 --app appnile --command \"COPY (SELECT * FROM player) TO STDOUT WITH CSV\" > file.csv")
#os.system("echo Done!")

#df = pd.read_csv("file.csv")
#print(df)

HEROKU_APP_NAME = "appnile"
TABLE_NAME = "player"
import subprocess, psycopg2

conn_info = subprocess.run(["heroku", "config:get", "DATABASE_URL", "-a", HEROKU_APP_NAME], stdout = subprocess.PIPE)
connuri = conn_info.stdout.decode('utf-8').strip()
conn = psycopg2.connect(connuri)
cursor = conn.cursor()
cursor.execute(sql.SQL("SELECT COUNT(*) FROM {};").format(sql.Identifier(TABLE_NAME)))
count = cursor.fetchall()
print(count)