from flask import Flask
import string
import random
import csv

app = Flask(__name__)
@app.route("/generate_password")
def generate_password():
    ascii_lowercase = string.ascii_lowercase
    ascii_uppercase = string.ascii_uppercase
    digit = string.digits
    special_symbols = string.punctuation
    str = string.ascii_letters + digit
    len = random.randint(10, 20)

    result = ""
    result += random.choice(ascii_uppercase)
    result += random.choice(ascii_lowercase)
    result += random.choice(special_symbols)
    result += random.choice(digit)
    for _ in range(len -4):
        result += random.choice(str)
    result1 = ""
    for i in range(len):
        ch = random.choice(result)
        result1 += ch
        j = result.find(ch)
        result = result[:j] + result[j+1:]

    return  "Password: " + result1

@app.route("/calculate_average")
def calculate_average():
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
    csv - use lib
    *pandas - use pandas for calculating
    """
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