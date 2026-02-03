from flask import Flask, request, render_template
from data_store import save_message, load_messages, search_by_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def post():
    name = request.form.get("name", "")
    message = request.form.get("message", "")
    save_message(name, message)

    return render_template("saved.html")

@app.route("/list")
def list_all():
    data = load_messages()
    return render_template("list.html", data=data)

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    results = search_by_name(keyword)
    return render_template("search.html", keyword=keyword, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

