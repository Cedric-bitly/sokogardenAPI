# import flask and its components
from flask import *

# import the pymysql module - it helps us to create a connection between python flask and mysql database
import pymysql

# import bcrypt
import bcrypt

# create a flask application and give it a name
app = Flask(__name__)


# below is the signup route
@app.route("/api/signup", methods = ["POST"])
def signup():
 if request.method=="POST":
  #extract the different details entered on the forms
  username = request.form["username"]
  email = request.form["email"]
  password = request.form["password"]
  phone = request.form["phone"]

  #by use of the print function lets print all those details sent with the upcoming request
  #print(username, email, password, phone)

 # hash the password using bcrypt
  hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

  # establish a connection between flask/python and mysql
  connection = pymysql.connect(host="localhost", user="root", password="",database="sokogardenonline")

  # create a cursor to execute the sql queries
  cursor = connection.cursor()


 #structure an sql to insert the details received from the form
 # The %s is a placeholder. It stands in place of actual values to be replaced later on
  sql = "INSERT INTO users(username,email,phone,password) VALUES(%s, %s, %s, %s)"

 # create a tuple that will hold all the data gotten from the form
  data = (username, email, phone, hashed_password)

 # by use of the cursor, execute the sql as you replace with the actual values
  cursor.execute(sql, data)

 # commit the changes to the database
  connection.commit()

  return jsonify({"message" : "User registered successfully"})


# below is the login/sign in route.
@app.route("/api/signin", methods=["POST"])
def signin():
    if request.method=="POST":
      #extract the two credentials entered
      email = request.form["email"]
      password = request.form["password"]

      #print out the details entered
      #print(email, password)

      #create/establish a connection to the database
      connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")

      #create a cursor 
      cursor = connection.cursor(pymysql.cursors.DictCursor)

      #structure the sql query that will check whether the email and pasword entered are correct
      sql = "SELECT * FROM users WHERE email = %s"


      #  put the data received from the form into a tuple
      data = (email,)

      # by use of the cursor execute the sql
      cursor.execute(sql, data)

      # check whether there are rows returned and store the same on a variable
      count = cursor.rowcount
      #print(count)

      #if there are records return it means th
    if count == 0:
        return jsonify({"message" : "login failed"})
    else:
        user = cursor.fetchone()
    
    # verify the password against the hash in the database
    if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
        user.pop("password")  # hide password from response
        return jsonify({"mesaage" : "User logged in successfully", "user": user})
    else:
        return jsonify({"message" : "login failed - wrong password"})


      # if there are records returned it means the email and the password are correct otherwise it means they are wrong
       





  







# run the application 
app.run(debug=True)