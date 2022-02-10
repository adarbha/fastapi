import os
import json
import pymssql
import random
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()


# domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message": "Hello TutLinks.com"}


@app.get("/run_query/")
def run_sql_query():
    with pymssql.connect(os.getenv("SERVER"), os.getenv("DVSUSERNAME"), os.getenv("PASSWORD"),
                         os.getenv("DEV_DB")) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute("SELECT TOP 5 CustomerID, CompanyName from SalesLT.Customer")
            rows = cursor.fetchall()
            return json.dumps(rows[random.choice(range(5))])


if __name__ == "__main__":
    print(run_sql_query())
