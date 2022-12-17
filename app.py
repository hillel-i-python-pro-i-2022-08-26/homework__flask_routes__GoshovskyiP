import csv
import json

import requests as requests
from flask import Flask

from applications.generate_users import generate_users
from settings.constants import FILES_PATH

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>HW 1 - Flask Routes</h1>"


@app.route("/requirements/")
def print_text():
    path = FILES_PATH.joinpath("text_file.txt")
    return f"<p>{path.read_text()}</p>"


@app.route("/generate-users/")
def generate_people():
    generated_data = "".join(
        f"<li>{user.name}@gmail.com</li>" for user in generate_users()
    )
    return f"<ol>{generated_data}</ol>"


@app.route("/space/")
def qty_of_space_crew() -> str:
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    text = response.text
    json_file = json.loads(text)
    return f"QTY of the people in the space crew: {json_file['number']}"


@app.route("/mean/")
def calculate_people_parameters() -> str:
    average_height = 0
    average_weight = 0
    row_counter = 0

    with open("people_data.csv", mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            average_height += float(list(row.values())[1]) * 2.54
            average_weight += float(list(row.values())[2]) * 0.45
            row_counter += 1
        return (
            f"<p>Average height is: {round(average_height / row_counter, 2)} cm</p>"
            f"<p>Average weight is: {round(average_weight / row_counter, 2)} kg</p>"
        )


if __name__ == "__main__":
    app.run(debug=True)
