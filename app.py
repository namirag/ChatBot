from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
qa_pipeline = pipeline("question-answering")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    question = data["question"]
    context = data["context"]

    # Get answer using the model
    answer = qa_pipeline(question=question, context=context)

    return jsonify(answer)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # use_reloader=False to prevent Flask from starting in multiple threads
