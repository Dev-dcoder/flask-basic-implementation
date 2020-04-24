from flask import Flask ,render_template ,request
import datetime


app = Flask(__name__)

@app.route("/")
def index():
    headline = " Welcome to my web page"
    #return f"<h1>Hello India</h1>"
    #return render_template("index.html")
    return render_template("index1.html",headline = headline)

@app.route("/bye")
def bye():
    headline = "Good Bye !!"
    return render_template("index1.html",headline = headline)

@app.route("/<string:name>")
def helo(name):
    return(f"hello , {name}!")

@app.route("/chkday")
def chkday():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.date == 1
    return render_template("index2.html",new_year=new_year)

@app.route("/lupchk")
def lopchk():
    names = ["Dev","Raj","Viaan"]
    return render_template("index3.html",names=names)

@app.route("/frst")
def first():
    return render_template("index4.html")

@app.route("/secnd")
def secnd():
    return render_template("index5.html")

@app.route("/chkhlo")
def abc():
    return render_template("chkhlo.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)



if __name__ == '__main__':
   app.run()
 