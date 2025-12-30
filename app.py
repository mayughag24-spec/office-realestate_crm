
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)



@app.route('/unit_booking')
def unit_booking():
    return render_template('unit_booking.html')

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/leads/add")
def add_lead():
    return render_template("add_lead.html")

@app.route("/leads/view")
def view_leads():
    return render_template("view_leads.html")

@app.route("/customers")
def customers():
    return render_template("customers.html")

@app.route("/payments")
def payments():
    return render_template("payments.html")

if __name__ == "__main__":
    
    

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="realestate_crm"
    )

@app.route("/")
def booking():
    return render_template("unit_booking.html")
app.run()
