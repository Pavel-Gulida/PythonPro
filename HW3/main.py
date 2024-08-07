from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import validate, fields
import requests
from faker import Faker
import csv

app = Flask(__name__)

@app.route("/generate_students")
@use_kwargs(
    {
        "count" : fields.Int(
            missing = 30,
            validate = [validate.Range(max=100)]
        )
    },
    location="query"
)
def generate_students(count):
    fake = Faker()
    with open("csvfile", "w",  newline="") as csvfile:
         writer = csv.DictWriter(csvfile,
            fieldnames= ["first_name","last_name","email","password","birthday"])
         writer.writeheader()
         result = ""
         for _ in range(count):
            student = dict()
            student["first_name"] = fake.first_name()
            student["last_name"] = fake.last_name()
            student["email"] = fake.email()
            student["password"] = fake.password()
            student["birthday"] = fake.date_of_birth(minimum_age=18, maximum_age=60)
            writer.writerow(student)
            result += str(student) + "<p>"
         return result.replace("}","").replace("{","").replace("'","")

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
    rates = requests.get(f"https://bitpay.com/api/rates/{currency}", params={}).json()
    currencies = requests.get(f"https://test.bitpay.com/currencies", params={}).json()
    result = round(rates["rate"] * convert, 2)
    for row in currencies["data"]:
        if row["code"] == currency:
            currency += f" ({row["symbol"]})"

    return f"{result} {currency} to buy {convert} Bitcoin"


if __name__ == "__main__":
    app.run(
        port=5000
    )
