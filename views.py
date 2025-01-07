from flask import Blueprint, render_template

my_view = Blueprint("my_view", __name__)


@my_view.route("/")
def index():
    return render_template("index.html")


@my_view.route("/page2")
def page2():
    return render_template("page2.html")


@my_view.route("/page3")
def page3():
    return render_template("page3.html")


@my_view.route("/page4")
def page4():
    my_name = "Javeria"
    return render_template("page4.html", my_name = my_name)


if __name__ == "__main__":
    app.run(debug = True, port = 8000)