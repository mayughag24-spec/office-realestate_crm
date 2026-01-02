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

# ================= DASHBOARD =================
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

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



# ================= SAVE BOOKING =================
@app.route("/save_booking", methods=["POST"])
def save_booking():
    data = request.form
    db = get_db()
    cur = db.cursor()

    # -------- 1️⃣ Insert Booking --------
    cur.execute("""
        INSERT INTO unit_booking
        (booking_date, sales_executive, wing, floor, unit_type, unit_number,
         carpet, agreement_cost, gst, stamp_duty, registration,
         furniture_charges, actual_package, package_total, parking_type, source)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data.get("bookingDate"),
        data.get("salesExecutive"),
        data.get("wing"),
        data.get("floor"),
        data.get("unitType"),
        data.get("unitNumber"),
        data.get("carpet"),
        data.get("agreementCost"),
        data.get("gst"),
        data.get("stampDuty"),
        data.get("registration"),
        data.get("furnitureCharges"),
        data.get("actualPackage"),
        data.get("packageTotal"),
        data.get("parkingType"),
        data.get("source")
    ))

    booking_id = cur.lastrowid

    # -------- 2️⃣ Insert Applicants --------
    for i in [1, 2, 3]:
        if data.get(f"app{i}FirstName"):
            cur.execute("""
                INSERT INTO booking_applicants
                (booking_id, applicant_no, salutation, first_name,
                 middle_name, last_name, occupation, age, mobile,
                 email, pan, aadhaar, address)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                booking_id,
                i,
                data.get(f"app{i}Salutation"),
                data.get(f"app{i}FirstName"),
                data.get(f"app{i}MiddleName"),
                data.get(f"app{i}LastName"),
                data.get(f"app{i}Occupation"),
                data.get(f"app{i}Age"),
                data.get(f"app{i}Mobile"),
                data.get(f"app{i}Email"),
                data.get(f"app{i}PAN"),
                data.get(f"app{i}Aadhaar"),
                data.get(f"app{i}Address")
            ))

    # -------- 3️⃣ Insert Payment --------
    cur.execute("""
        INSERT INTO booking_payments
        (booking_id, booking_amount, payment_mode,
         cheque_trn_no, cheque_trn_date, bank_name)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        booking_id,
        data.get("bookingAmount"),
        data.get("paymentMode"),
        data.get("chequeNo"),
        data.get("chequeDate"),
        data.get("bankName")
    ))

    db.commit()
    cur.close()
    db.close()

    return redirect(url_for("dashboard"))

# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)
