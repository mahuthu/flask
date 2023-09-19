from flask import Flask, render_template

app = Flask(__name__)

class Jupyter:
    def __int__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
@app.route("/")
def hello():
    return render_template("hello.html", name="john doe", value="jinja2")


@app.route("/fancy")
def fancy():
    return """
    <html>
    <body>
    
    <h1>Greetimgs</h1>
    <p>hello world</p>
    </body>
    </html>
    """


@app.route("/expressions/")
def expressions():
    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "hare"

    # addition and interpolation
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "captain"
    last_name = "marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,

    }
    return render_template("jinja_expressions.html", **kwargs)
#or
#return render_template("jinja_expressions.html", color = color, animal_one = animal_one etc)

@app.route("/data/")
def render_data_structures():

    movies = ["top gun", "prey", "stranger things"]
    car = {"brand": "tesla", "model": "roadster", "year": "2017"}
    moons = Jupyter("one", "two", "three", "four")
    return render_template("data.html", movies=movies, car=car, moons=moons)



    # or
    #kwargs = {"movies": movies,
             # "car": car,
             # "moons": moons}

@app.route("/conditionals/")
def conditionals():
    company = "Microsoft"
    return render_template("conditionals.html", company=company)

@app.route("/booleans/")
def boolean():
    company = "Apple"
    return render_template("boolean.html", company=company)

@app.route("/for/")
def for_loop():
    elements = ["mercury","mars","earth","venus","jupyter","uranuas"]
    return render_template("for.html", planets = elements)


@app.route("/forcon/")
def for_conditional():
    user_os = {"bob": "Windows",
               "cain": "MacOS",
               "abel": "Linux",
               "paul": "Windows"}
    return render_template("for_condition.html", user_os=user_os)
