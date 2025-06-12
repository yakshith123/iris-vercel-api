import json
import joblib
import os

model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))

def handler(request):
    try:
        body = request.get_json()
        features = [
            body["sepal_length"],
            body["sepal_width"],
            body["petal_length"],
            body["petal_width"]
        ]
        prediction = model.predict([features])[0]
        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": int(prediction)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
