# 🎓 Student Performance Prediction Web App

An end-to-end Machine Learning project that predicts student academic performance through an interactive web application built with **Python, Scikit-learn, Pandas, NumPy, and Streamlit**.

The project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, model development, evaluation, and real-time predictions through a user-friendly interface.

## 📌 Project Overview

Student performance can be influenced by various academic and personal factors. This project explores the application of machine learning to student-related data to generate academic performance predictions.

The application combines a trained machine learning model with a Streamlit interface, making predictions accessible through a simple web-based experience.

## ✨ Key Features

- **Data Preprocessing:** Prepare student data for machine learning.
- **Feature Engineering:** Process relevant input features for prediction.
- **Machine Learning:** Develop and use a trained model for student performance prediction.
- **Model Evaluation:** Evaluate model performance as part of the ML workflow.
- **Interactive Web Interface:** Provide a simple interface using Streamlit.
- **Real-Time Predictions:** Generate predictions from user-provided inputs.
- **Data Handling:** Work with structured student data using Pandas and NumPy.
- **Model Persistence:** Store the trained model in `model.pkl` for reuse.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Machine learning and model evaluation |
| Pandas | Data processing and analysis |
| NumPy | Numerical operations |
| Streamlit | Interactive web application |
| Pickle | Storage and loading of the trained model |

## 🧠 Machine Learning Workflow

The project follows an end-to-end machine learning workflow:

1. **Data Preparation** – Load and prepare the student dataset.
2. **Data Preprocessing** – Transform data into a suitable format for model training and prediction.
3. **Feature Engineering** – Prepare relevant features for the learning process.
4. **Model Development** – Train and develop a machine learning model.
5. **Model Evaluation** – Assess predictive performance using appropriate evaluation methods.
6. **Model Persistence** – Save the trained model for reuse.
7. **Application Integration** – Connect the model with the Streamlit interface.
8. **Prediction** – Generate predictions through the web application.

## 📂 Project Structure

```text
student-performance-predictor/
│
├── app.py              # Streamlit web application
├── model.py            # Machine learning model logic
├── model.pkl           # Saved trained model
├── student_data.csv    # Student dataset
├── reports.csv         # Project report data
└── README.md           # Project documentation
```

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.9 or a compatible version
- pip package manager
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/narmadha2006/student-performance-predictor.git
```

### 2. Navigate to the Project Directory

```bash
cd student-performance-predictor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

If the repository does not contain a `requirements.txt` file, install the core dependencies:

```bash
pip install streamlit pandas numpy scikit-learn
```

### 5. Run the Application

```bash
streamlit run app.py
```

Once the application starts, open the local URL displayed in your terminal to access the web interface.

## 📊 Model Evaluation

Model evaluation is an important part of developing reliable machine learning solutions.

Depending on the prediction task, suitable evaluation metrics may include:

- **Regression:** MAE, MSE, RMSE, and R² score.
- **Classification:** Accuracy, Precision, Recall, F1-score, and Confusion Matrix.

The appropriate metrics depend on the target variable and the model implemented in this project. Actual evaluation results should be added here once verified.

## 🔮 Future Enhancements

- Deploy the application to a cloud platform.
- Add more detailed data visualizations.
- Improve model performance through additional experimentation.
- Include feature importance or model explainability.
- Add more comprehensive model evaluation reports.
- Improve input validation and prediction feedback.

## 🎯 Learning Outcomes

This project demonstrates practical experience in:

- Developing an end-to-end machine learning application.
- Processing and analyzing structured datasets.
- Working with Scikit-learn models.
- Saving and reusing trained machine learning models.
- Integrating machine learning with Streamlit.
- Building interactive, data-driven applications using Python.

## 👩‍💻 Author

**Narmadha**

GitHub: [@narmadha2006](https://github.com/narmadha2006)

## ⭐ Acknowledgements

Thank you for visiting this project! If you find it useful or interesting, consider giving the repository a star.

---

*Developed using Python, Scikit-learn, Pandas, NumPy, and Streamlit.*
