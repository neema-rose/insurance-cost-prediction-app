import streamlit as st
from prediction_helper import predict
import base64

# ---------------- IMAGE LOADER ----------------
def load_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = load_image(
    r"C:\Users\91994\codebasics_machine_learning\Healthcare_Premium_Prediction\Healthcare_Premium_Prediction_App\Insurance_image.jpg"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
    .main {
        background-color: #f9fafb;
    }
    h1 {
        text-align: center;
        color: #2c3e50;
    }

    /* LEFT COLUMN IMAGE – ALIGNED RIGHT */
    .image-box {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        height: 100%;
        min-height: 420px;
        padding-right: 1rem;
    }

    .image-box img {
        max-height: 300px;
        width: auto;
        object-fit: contain;
        border-radius: 10px;
    }

    /* BUTTON STYLING */
    .stButton > button {
        background-color: #2c7be5;
        color: white;
        border-radius: 5px;
        height: 2.0em;
        width: 250px;
        font-size: 15px;
        margin-top: 0.2rem;
    }

    .stButton > button:hover {
        background-color: #1a68d1;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title('Health Insurance Cost Predictor')

# ---------------- LAYOUT: IMAGE + FORM ----------------
left_col, right_col = st.columns([1, 2])

with left_col:
    st.markdown(
        f"""
        <div class="image-box">
            <img src="data:image/webp;base64,{img}">
        </div>
        """,
        unsafe_allow_html=True
    )

with right_col:

    categorical_options = {
        'Gender': ['Male', 'Female'],
        'Marital Status': ['Unmarried', 'Married'],
        'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
        'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
        'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
        'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
        'Medical History': [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ],
        'Insurance Plan': ['Bronze', 'Silver', 'Gold']
    }

    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

    with row3[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row3[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row3[2]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

    with row4[0]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'])
    with row4[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# ---------------- INPUT DICTIONARY ----------------
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# ---------------- PREDICTION ----------------
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f'Predicted Health Insurance Cost: {prediction}')


    
