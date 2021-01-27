from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "hello wellcome"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/<name>/<int:number>")
def test(name,number):
    return f"Hello {name} and {number}"



if __name__=="__main__":
    app.run(debug=True)