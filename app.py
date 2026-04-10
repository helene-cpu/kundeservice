from flask import Flask, render_template, redirect, session, request
import mysql.connector
from forms import ComplainForm, RegisterForm, LoginForm, AnswerForm
from werkzeug.security import check_password_hash, generate_password_hash

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
        epost = form.epost.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
        "INSERT INTO saker (Tittel, epost,  Kategori, Ordrenummer, Beskrivelse) VALUES (%s, %s, %s, %s, %s)",
         (title, epost, category, ordernumber, description)
        )

        conn.commit()
        cur.close()
        conn.close()

        return redirect("/sendt")

    return render_template("send.html", form=form)

@app.route('/sendt')
def sendt():
    return render_template("sendt.html")

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        brukernavn = form.brukernavn.data
        passord = form.passord.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT Navn, Passord FROM brukere WHERE brukernavn= %s",
            (brukernavn,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            navn_db = user[0]
            passord_db = user[1]

            if check_password_hash(passord_db, passord):
                session['navn'] = navn_db
                return redirect("/admin")
    
            else:
                form.brukernavn.errors.append("Feil brukernavn eller passord")

        else:
            form.brukernavn.errors.append("Feil brukernavn eller passord")

    return render_template("logginn.html", form = form)

@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        navn = form.navn.data
        brukernavn = form.brukernavn.data
        passord = form.passord.data

        passord_hash = generate_password_hash(passord)

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO brukere (Navn, Brukernavn, Passord) VALUES (%s, %s, %s)",
            (navn, brukernavn, passord_hash)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        return redirect('/login')

    return render_template("register.html", form= form)


@app.route('/admin', methods=["POST", "GET"])
def admin():
    if 'navn' not in session:
        return redirect('/login')

    form = AnswerForm()

    if form.validate_on_submit():
        svar = form.svar.data
        sak_id = request.form.get('sak_id')

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
           "UPDATE saker SET Svar = %s, Status='Closed' WHERE Sak_ID = %s",
           (svar, sak_id)
        )

        conn.commit()
        cur.close()
        conn.close()

        return redirect ("/admin")

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT Tittel, Kategori, Ordrenummer, Beskrivelse, Sak_ID FROM saker WHERE Svar IS NULL"
    )

    saker = cur.fetchall()

    cur.close()
    conn.close()
    
    
    return render_template("admin.html", saker=saker, form = form)

if __name__ == "__main__":
    app.run(debug=True)