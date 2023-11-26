from flask import Flask, render_template

from models import db, connect_to_db, Donor, User

app = Flask(__name__)

@app.route("/")
def index():
    donors = User.query.get(1).donors
    return render_template("dashboard.html", donors=donors)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)