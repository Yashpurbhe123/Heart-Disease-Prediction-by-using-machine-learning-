import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
working_dir = os.path.dirname(os.path.abspath(__file__))


heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)


if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex : (0) - Female , (1) - Male')

    with col3:
        cp = st.text_input('Chest Pain types [ 0: Normal 1: Unusual 2: Not heart 3: No pain.]')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar [ 1: > 120 mg/dL , 0: ≤ 120 mg/dL ]')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic(ECG) results [ 0: Normal 1: Abnormal ]')

    with col2:
        thalach = st.text_input('Highest heart rate reached')

    with col3:
        exang = st.text_input('Exercise-caused chest pain.[ 0: NO 1: Yes ] ')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('ST wave shape during exercise [ 0: Upsloping , 1: Flat , 2: Downsloping ]')

    with col3:
        ca = st.text_input('"Vessels shown by X-ray":0: None, 1: One, 2: Two, 3: More')

    with col1:
        thal = st.text_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect')

    heart_diagnosis = ''


    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
