from flask import Flask, render_template
from forms import ComplainForm

app = Flask (__name__)
app.config["SECRET_KEY"] = "superduperekstrahemmelig123"

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/send', methods=["GET", "POST"])
def send():
    form = ComplainForm()
    return render_template("send.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)