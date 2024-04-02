from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/anotherpage")
def anotherpage():
    name = "Bill Gates"

    if request.method == 'GET':
        return render_template('somehtmlpage.html', name=name)


if __name__ == "__main__":
    app.run()
    # app.run(debug=True, passthrough_errors=True, use_reloader=False, host=host, port=port)