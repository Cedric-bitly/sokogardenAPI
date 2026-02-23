# import flask and its components
from flask import *
import os

# import the pymysql module - it helps us to create a connection between python flask and mysql database
import pymysql



# create a flask application and give it a name
app = Flask(__name__)


#configure the location to where your product images will be saved on your application.
app.config["UPLOAD_FOLDER"] = "static/images"

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

 
  # establish a connection between flask/python and mysql
  connection = pymysql.connect(host="localhost", user="root", password="",database="sokogardenonline")

  # create a cursor to execute the sql queries
  cursor = connection.cursor()


 #structure an sql to insert the details received from the form
 # The %s is a placeholder. It stands in place of actual values to be replaced later on
  sql = "INSERT INTO users(username,email,phone,password) VALUES(%s, %s, %s, %s)"

 # create a tuple that will hold all the data gotten from the form
  data = (username, email, phone, password)

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
      data = (email, password)

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
    

        return jsonify({"mesaage" : "User logged in successfully", "user": user})
   


      # if there are records returned it means the email and the password are correct otherwise it means they are wrong
       





  
#below is the route for adding products
@app.route("/api/add_product", methods=["POST"])
def Addproducts():
   if request.method == "POST":
      #extract the data entered on the form
      product_name = request.form["product_name"]
      product_description = request.form["product_description"]
      product_cost = request.form["product_cost"]
      #for the product photo, we shall fetch it from files as shown below.
      product_photo  = request.files["product_photo"]

      #extract the filename of the producy_photo
      filename = product_photo.filename
      #by use of the os module we can extract the file path where the image is currently saved
      photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        # print("This is the photo path: ", photo_path)

      #save the product_photo image into the new location
      product_photo.save(photo_path)

      #print them out to test whether we are receiving the details sent with the request
      #print(product_name, product_description, product_cost, product_photo)
      #establish a connection to the db
      connection = pymysql.connect(host="localhost", user="root", password="",database="sokogardenonline")

      #create a cursor
      cursor  = connection.cursor()

      #structure the sql query that will insert the details from the form
      sql = "INSERT INTO product_details(product_name,product_description,product_cost,product_photo) VALUES(%s, %s, %s, %s)"

      # create a tuple that will hold all the data which are held onto the different variables declared.
      data = (product_name,product_description,product_cost,filename)

      # by use of the cursor, execute the sql as you replace with the actual values
      cursor.execute(sql, data)

      # commit the changes to the database
      connection.commit()

      return jsonify({"message" : "Product added successfully"})
      
      #return jsonify({"message" : "Add product route accessed"})



#below is the route for getting products
@app.route("/api/get_products", methods=["GET"])
def Getproducts():
    #establish a connection to the db
    connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")
    
    #create a cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    #structure the sql query to get all products
    sql = "SELECT * FROM product_details"
    
    #execute the query
    cursor.execute(sql)
    
    #fetch all the results
    products = cursor.fetchall()
    
    #return the products as json
    return jsonify(products)





# run the application 
app.run(debug=True)