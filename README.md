# 🌸 Iris Flower Prediction API

A simple machine learning API that predicts the species of an iris flower based on its measurements.  
Built using **Python**, **Flask**, and **scikit-learn**, and ready to deploy on **Heroku**, **Vercel**, **Render**, or **Railway**.

---

## 🚀 live :https://iris-vercel-api-git-main-yakshith-s-ys-projects.vercel.app

**POST** `/predict`

**Request JSON:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Features
✅ Pre-trained model using scikit-learn

✅ Flask API with one prediction route

✅ JSON input/output

✅ Deployable on major platforms


git clone https://github.com/your-username/iris-flask-api.git
cd iris-flask-api
pip install -r requirements.txt
python app.py

 Requirements
Python 3.8+

Flask

scikit-learn

gunicorn (for production)


CI/CD and Automated Tests 🔹
This project includes Continuous Integration and Continuous Deployment (CI/CD) practices to demonstrate production readiness.

✅ Continuous Integration (Github Actions):

A Github Action pipeline is configured in [.github/workflows/python-app.yml].

This pipeline performs the following:

Sets up the appropriate Python environment.

Installs the project’s dependencies.

Executes automated tests (with pytest) to validate functionality.

✅ Automated Tests:

We have a test script test_app.py that validates API functionality by sending a request to the API and verifying the response.

This guarantees code quality and prevents regressions.

🔹 How to Run Tests Locally 🔹
bash
Copy
Edit
pip install -r requirements.txt
pytest

✅ All tests should pass with a green output.

🔹 How CI Works 🔹
Every new push or pull request to main:

Github Actions runs:

Installs dependencies.

Performs automated tests.

If all checks pass, the code is ready for deployment (Heroku, Render, or another platform).
