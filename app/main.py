import logging
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from app.indexing import load_or_create_index
from app.query import build_query_engine, run_query

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

index = load_or_create_index()
query_engine = build_query_engine(index)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data["question"]
    result = run_query(query_engine, question)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, port=5000)
