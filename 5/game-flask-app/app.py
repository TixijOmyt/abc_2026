from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """" Вместо строки вывожу содержимое html файла """
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/post_list")
def post_list():
    return render_template("post_list.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
