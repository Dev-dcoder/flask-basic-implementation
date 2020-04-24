from flask import Flask , render_template ,request ,session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
@app.route("/aa",methods=["GET","POST"])
def aa():
    if request.method =="POST":
        note = request.form.get("note")
        print("Dev===",note)
        notes.append(note)
    print("====",notes)
    return render_template("indexx.html",notes=notes)

if __name__ == "__main__":
    app.run()