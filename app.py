from flask import Flask, render_template, request, jsonify
from rag.rag_pipeline import CVRAG

app = Flask(__name__)
rag = CVRAG()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_question = request.json["message"]
    answer = rag.ask(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
