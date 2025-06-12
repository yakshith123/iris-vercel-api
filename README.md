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
