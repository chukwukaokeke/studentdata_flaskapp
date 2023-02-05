from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route("/index")
def index():
    # Connect to the database
    cnx = mysql.connector.connect(username=os.getenv("mysqlusername"), password=os.getenv("mysqlpassword"), host='127.0.0.1', database='studentdatabase')
    cursor = cnx.cursor()

    # Select all data from the "studenttable"
    query = "SELECT name, score, class FROM studenttable"
    cursor.execute(query)
    student_data = cursor.fetchall()

    # Close the connection
    cursor.close()
    cnx.close()

    # Render the template and pass the data to it
    return render_template("index.html", student_data=student_data)

if __name__ == "__main__":
    app.run(debug=True)
