Flask MySQL Student Database App
This is a Flask web application that connects to a MySQL database and retrieves data from a table called studenttable. The data is then passed to a template and displayed on a webpage.

<h1>Requirements</h1>
Flask
mysql-connector-python
Usage
Set the environment variables mysqlusername and mysqlpassword with the username and password for your MySQL database.

Run the app with python app.py and visit http://127.0.0.1:5000/index in your web browser to view the student data.

File Structure
app.py: The main file that contains the Flask app and routing code.

templates/index.html: The HTML template file that displays the student data.