from flask import Flask, render_template, request
from pymongo import MongoClient
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["projectDataBase"]
collection = db["information"]  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Store user information in MongoDB
        user_data = {"name": name, "email": email}
        collection.insert_one(user_data)
        # Render confirmation page
        return render_template('confirmation.html', name=name, email=email)
    return render_template('LoginPage.html')

if __name__ == '__main__':
    app.run(debug=True)




