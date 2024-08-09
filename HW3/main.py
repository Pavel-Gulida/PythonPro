from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields
import requests
from faker import Faker
import csv

app = Flask(__name__)

@app.route("/generate_students")
def generate_students():
    fake = Faker()
    with open("csvfile", "w", newline="") as csvfile:
         writer = csv.DictWriter(csvfile,
            fieldnames= ["first_name","last_name","email","password","birthday"])
         writer.writeheader()

         for _ in range(1000):
            student = dict()
            student["first_name"] = fake.first_name()
            student["last_name"] = fake.last_name()
            student["email"] = fake.email()
            student["password"] = fake.password()
            student["birthday"] = fake.date_of_birth(minimum_age=18, maximum_age=60)
            writer.writerow(student)
            
    with open("csvfile", "r") as csvfile:
        return csvfile.read().replace("\n","<p>")

@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency" : fields.Str(
            missing = "USD"
        ),
        "convert" : fields.Int(
            missing = 1
        )
    },
    location="query"
)
def get_bitcoin_value(currency, convert):
    rates = requests.get("https://bitpay.com/api/rates", params={}).json()
    currencies = requests.get("https://test.bitpay.com/currencies", params={}).json()
    result = 0
    for d in rates:
        if d["code"] == currency:
            result = round(d["rate"] * convert, 2)
    for d in currencies["data"]:
        if d["code"] == currency:
            currency += f" ({d["symbol"]})"

    return f"{result} {currency} to buy {convert} Bitcoin"


if __name__ == "__main__":
    app.run(
        port=5000
    )
