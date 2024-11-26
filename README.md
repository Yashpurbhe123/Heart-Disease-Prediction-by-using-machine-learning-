# **Heart Disease Prediction Using Machine Learning**

This project utilizes machine learning algorithms to predict the likelihood of heart disease based on patient data. It features a Streamlit web application that allows users to input patient data and receive a prediction. The app uses four different machine learning models, and the one with the highest accuracy, Logistic Regression, is employed for prediction.

## **Features**

- **User Input Form**: The user can input patient data (such as age, cholesterol levels, blood pressure, etc.).
- **Model Prediction**: Based on the input, the app will predict the likelihood of heart disease using a trained model.
- **Comparison of Models**: The app compares the performance of four models—Logistic Regression, Random Forest, Decision Tree, and K-Nearest Neighbors—and highlights the best-performing model.
- **Real-time Results**: The app displays the prediction for heart disease and the model's accuracy in real-time.

## **Machine Learning Models**

The following models were used to predict heart disease:

1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Decision Tree Classifier**
4. **K-Nearest Neighbors (KNN) Classifier**

Among these, **Logistic Regression** achieved the highest accuracy of **88.18%** and was selected as the final model.

## **Steps in the Project**

1. **Data Loading and Exploration**:  
   The dataset is loaded, and initial exploratory data analysis (EDA) is performed.

2. **Data Preprocessing**:  
   Target variable separation, feature extraction, and splitting the data into training and testing sets.

3. **Model Training**:  
   Various machine learning models are trained on the training data, and their performance is evaluated.

4. **Model Evaluation**:  
   The trained models are tested on the testing data, and the best-performing model is selected for prediction.

## **Getting Started**

### **Pre-requisites**

Before running the app, make sure you have the following libraries installed:

```bash
pip install streamlit scikit-learn pandas
```

### **Running the App**

1. Clone this repository to your local machine.

2. Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

3. Open your web browser and go to `http://localhost:8501` to interact with the app.

### **App Features**

- **Input**: Users can input their data such as age, cholesterol, blood pressure, and other health metrics.
- **Prediction**: The app will predict the likelihood of heart disease based on the input data.
- **Evaluation**: It will also show the accuracy of the model and the prediction result.

## Conclusion

This project demonstrates the power of machine learning in healthcare by providing a predictive tool for heart disease detection. It can assist healthcare professionals in making informed decisions and improving patient outcomes.