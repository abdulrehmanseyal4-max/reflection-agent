from flask import Flask, render_template, request, jsonify
from main import run_agent  # import your reflection agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # call your reflection-agent
    bot_reply = run_agent(user_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
