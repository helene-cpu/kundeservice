from flask import Flask, render_template, redirect
import mysql.connector
from forms import ComplainForm

app = Flask (__name__)
app.config["SECRET_KEY"] = "superduperekstrahemmelig123"

def get_conn():
    return mysql.connector.connect(
        host = "localhost",
        user = "kundeservice",
        password = "Kdhmjth1234#",
        database = "kundeservice"
)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/send', methods=["GET", "POST"])
def send():
    form = ComplainForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        ordernumber = form.ordernumber.data
        description = form.description.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
        "INSERT INTO saker (Tittel, Kategori, Ordrenummer, Beskrivelse) VALUES (%s, %s, %s, %s)",
         (title, category, ordernumber, description)
        )

        conn.commit()
        cur.close()
        conn.close()

        return redirect("/sendt")

    return render_template("send.html", form=form)

@app.route('/sendt')
def sendt():
    return render_template("sendt.html")

if __name__ == "__main__":
    app.run(debug=True)