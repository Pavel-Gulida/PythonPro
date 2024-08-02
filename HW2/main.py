from flask import Flask
import string
import random
import csv

app = Flask(__name__)
@app.route("/generate_password")
def generate_password():
    str = string.ascii_letters + string.digits
    len = random.randint(10, 20)

    result = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)
    result += random.choice(string.punctuation) + random.choice(string.digits)
    for _ in range(len - 4):
        result += random.choice(str)

    result = list(result)
    random.shuffle(result)
    result = "".join(result)

    return  f"Password: {result}"

@app.route("/calculate_average")
def calculate_average():

    with open('hw.csv', "r") as csvfile:
        reader = csv.DictReader(csvfile)
        average_high = 0
        average_weight = 0
        length = 0
        for row in reader:
            average_high += float(row[" Height(Inches)"])
            average_weight += float(row[" Weight(Pounds)"])
            length += 1
        average_high = round(average_high/length,3)
        average_weight = round(average_weight/length,3)

        return (f"Average high: {average_high} Inches | "
                f"Average weight: {average_weight} Pounds")


if __name__ == "__main__":
    app.run(
        port=5000, debug=True
    )