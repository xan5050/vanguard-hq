from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    super_name = another_method("Camden")
    return "<p>Hello, World!</p>"
    

def another_method(name):
    name = "super" + name
    return name

@app.route("/bob", methods = ['POST'])
def bob():
    return "bob"


@app.route("/<name>")
def super_name(name):   
    name = another_method(name)
    return name

@app.route("/link") 
def links():
    list1 = url_for(super_name)
    return list1



if __name__ == "__main__":
    app.run()


