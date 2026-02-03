from flask import Flask, request, jsonify
from langchain_core.messages import HumanMessage
from graph import app as debugger_app
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(flask_app) 

@flask_app.route("/debug", methods=["POST"])
def debug():
    data = request.json

    code = data.get("code")
    query = data.get("query")

    initial_state = {
            "messages": [
                HumanMessage(
                    content=f"""
        User request:
        {query}

        Code:
        {code}
        """
                )
            ],
            "code": code,
            "language": ""
        }


    result = debugger_app.invoke(initial_state)

    return jsonify({
        "response": result["messages"][-1].content
    })


if __name__ == "__main__":
    flask_app.run(debug=True)
