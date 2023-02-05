<h1>Flask MySQL Student Database App</h1>
This is a Flask web application that connects to a MySQL database and retrieves data from a table called studenttable. The data is then passed to a template and displayed on a webpage.

<h2>Requirements</h2>
Flask
mysql-connector-python

<h2>Usage</h2>
Set the environment variables mysqlusername and mysqlpassword with the username and password for your MySQL database.

Run the app with python app.py and visit http://127.0.0.1:5000/index in your web browser to view the student data.

<h2>File Structure</h2>
app.py: The main file that contains the Flask app and routing code.

templates/index.html: The HTML template file that displays the student data.

<h1>Notes</h1>
The database must have a table named studenttable with columns name, score, and class.

The debug argument in app.run() is set to True for development purposes only. In a production environment, it should be set to False.
