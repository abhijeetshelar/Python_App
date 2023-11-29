# app.py
from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        location = request.form['location']

        with open('user_data.csv', 'a', newline='') as csv_file:
            fieldnames = ['Username', 'Location']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if csv_file.tell() == 0:
                writer.writeheader()

            writer.writerow({'Username': username, 'Location': location})

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
