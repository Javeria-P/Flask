from flask import Flask
from views import my_view


app = Flask (__name__)
app.register_blueprint(my_view)

#@app.route("/")
#def index():
    #return render_template("index.html")
    #return"<h1>Hello, World!</h1>"



#@app.route("/page2")
#def page2():
    #return render_template("page2.html")
    #return"<h1>Hello, World From My Second Page</h1>"


#@app.route("/page3")
#def page3():
    #return render_template("page3.html")
    #return"<h1>Hello, and welcome to third page.</h1>"


#@app.route("/page4")
#def page4():
    #my_name = "Javeria"
    #return render_template("page4.html", my_name = my_name)
    #return f"My name is {my_name}."

if __name__ == "__main__":
    app.run(debug = True, port = 8000)


