from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Office Real Estate CRM</h2>
    <p>CRM Home Dashboard is running successfully 🚀</p>
    """

if __name__ == "__main__":
    app.run()
