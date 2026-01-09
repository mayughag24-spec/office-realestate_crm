from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ================= DATABASE CONNECTION =================
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="realestate_crm"
    )



# ================= LEADS =================
@app.route("/leads/add")
def add_lead():
    return render_template("add_lead.html")

@app.route("/leads/view")
def view_leads():
    return render_template("view_leads.html")

# ================= CUSTOMERS =================
@app.route("/customers")
def customers():
    return render_template("customers.html")

# ================= PAYMENTS =================
@app.route("/payments")
def payments():
    return render_template("payments.html")



