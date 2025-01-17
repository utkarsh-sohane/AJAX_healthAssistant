import streamlit as st
import os
import pickle
import numpy as np


st.set_page_config(
    page_title="AJAX - A Health Assistant",
    layout="wide",
    page_icon="🧑‍⚕️"
)


custom_css = """
<style>
   
.sidebar .sidebar-content {
    background-image: linear-gradient(#f5f5f5, #f5f5f5);
    color: black;
}
.subheader {  
    font-size: 20px;
    font-weight: bold;
    color: red;
    background-color: #f5f5f5;
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
}

</style>
"""      


st.markdown(custom_css, unsafe_allow_html=True)


st.title("AJAX - A Health Assistant")


working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(os.path.join(working_dir, 'diabetes_model.sav'), 'rb'))

heart_disease_model = pickle.load(open(os.path.join(working_dir, 'heart_disease_model.sav'), 'rb'))

parkinsons_model = pickle.load(open(os.path.join(working_dir, 'parkinsons_model.sav'), 'rb'))

liver_disease_model = pickle.load(open(os.path.join(working_dir, 'liver-disease.sav'), 'rb'))

asthma_disease_model_path = os.path.join(working_dir, 'asthma_disease.sav')

asthma_disease_model = pickle.load(open(os.path.join(working_dir, 'asthma_disease.sav'), 'rb'))



def main():

    menu = ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Liver Disease Prediction", "Asthma Disease Prediction"]
    selected = st.sidebar.selectbox("Menu", menu)

    if selected == "Home":
        st.subheader("Home")


        st.write("Welcome to Health Assistant! This application is designed to help you predict the likelihood of having diabetes, heart disease, or Parkinson's disease. Please select the appropriate option from the sidebar to get started.The application uses machine learning models to make predictions based on the input data provided by the user The models have been trained on real-world data and are designed to provide accurate predictions based on the input features")
        st.write("To get started, simply select the appropriate option from the sidebar menu and follow the instructions to enter the required input data. The application will then use the selected machine learning model to make a prediction and display the results.")
        st.subheader("Thank you for using Health Assistant! We hope you find the application helpful and informative. If you have any questions or feedback, please feel free to contact us.")
        

        st.subheader("Team Members")
        st.write("1. Name: Abhishek Nangare,  Reg No: 21BAI10060")
        st.write("2. Name: Kanhaiya Agrwal,  Reg No: 21BAI10241")
        st.write("3. Name: Utkarsh Sohane,  Reg No: 21BCE11329")
        st.write("4. Name: Shaz Alam,  Reg No: 21BCY10221")
        st.write("5. Name: Akshay,  Reg No: 21BCE10381")
        st.write("6. Name: Om Saxena, Reg No: 21BCE11517")
        st.write("7. Name: Upendra Kumar, Reg No: 21BCE11554")
        

        
        


    elif selected == "Diabetes Prediction":
        st.subheader("Diabetes Prediction")
        predict_diabetes(diabetes_model)
        display_diabetes_faq()

    elif selected == "Heart Disease Prediction":
        st.subheader("Heart Disease Prediction")
        predict_heart_disease(heart_disease_model)
        display_heart_disease_faq()

    elif selected == "Parkinson's Prediction":
        st.subheader("Parkinson's Prediction")
        predict_parkinsons(parkinsons_model)
        display_parkinsons_faq()

    elif selected == "Liver Disease Prediction":
        st.subheader("Liver Disease Prediction")
        predict_liver_disease(liver_disease_model)
        display_liver_disease_faq()


    elif selected == "Asthma Disease Prediction":
        st.subheader("Asthma Disease Prediction")
        predict_asthma_disease(asthma_disease_model) 
        display_asthma_disease_faq()       


def predict_diabetes(model):
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level (mg/dL)')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value (mmHg)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value (in mm)')

    with col2:
        Insulin = st.text_input('Insulin Level (IU/ml)')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person (in years)')


    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic.'
        else:
            diab_diagnosis = 'The person is not diabetic.'

        st.subheader("Diabetes Prediction Result:")
        #st.write(diab_diagnosis)
        st.write("Please note that the prediction is based on the input data provided and may not be accurate in all cases. It is always recommended to consult a healthcare professional for proper diagnosis and treatment.")

    st.success(diab_diagnosis)

def predict_heart_disease(model):
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (in years)')

    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])

    with col3:
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mmHg)')

    with col2:
        chol = st.text_input('Serum Cholestoral (in mg/dl)')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'])

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved during stress test')

    with col3:
        exang = st.selectbox('Exercise Induced Angina(Chest pain)', ['Yes', 'No'])

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'])

    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', ['0', '1', '2', '3'])

    with col1:
        thal = st.selectbox('Thal', ['Normal', 'Fixed Defect', 'Reversable Defect'])

  
    heart_diagnosis = ''

   
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        

        user_input = [float(x) if x.replace('.', '', 1).isdigit() else 0 for x in user_input]

        heart_prediction = model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease.'
        else:
            heart_diagnosis = 'The person does not have any heart disease.'
        
        st.subheader("Heart Disease Prediction Result:")
        #st.write(heart_diagnosis)
        st.write("Please note that the prediction is based on the input data provided and may not be accurate in all cases. It is always recommended to consult a healthcare professional for proper diagnosis and treatment.")

    st.success(heart_diagnosis)

def predict_parkinsons(model):

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_Fo = st.text_input('MDVP_Fo(Hz)')

    with col2:
        MDVP_Fhi = st.text_input('MDVP_Fhi(Hz)')

    with col3:
        MDVP_Flo = st.text_input('MDVP_Flo(Hz)')

    with col1:
        MDVP_Jitter_Per = st.text_input('MDVP_Jitter(%)')

    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')

    with col3:
        MDVP_RAP = st.text_input('MDVP_RAP (in ms)')

    with col1:
        MDVP_PPQ = st.text_input('MDV_PPQ (in ms)')

    with col2:
        Jitter_DDP = st.text_input('Jitter_DDP (in ms)')

    with col3:
        MDVP_Shimmer = st.text_input('MDVP_Shimmer')

    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP_Shimmer(dB)')

    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer_APQ3')

    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer_APQ5')

    with col1:
        MDVP_APQ = st.text_input('MDVP_APQ')

    with col2:
        Shimmer_DDA = st.text_input('Shimmer_DDA (in ms)')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

  
    parkinsons_diagnosis = ''

  
    if st.button("Parkinson's Test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_Per, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                      MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE,
                      DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's Disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's Disease."
        
        st.subheader("Parkinson's Disease Prediction Result:")
        #st.write(parkinsons_diagnosis)
        st.write("Please note that the prediction is based on the input data provided and may not be accurate in all cases. It is always recommended to consult a healthcare professional for proper diagnosis and treatment.")
  

    st.success(parkinsons_diagnosis)


    
def predict_liver_disease(model):
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            Age = st.text_input('Age')
    
        with col2:
            Gender = st.text_input('Gender')

        with col3:
            Total_Bilirubin = st.text_input('Total Bilirubin')


        with col1:
            Direct_Bilirubin = st.text_input('Direct Bilirubin')

        with col2:
            Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase')

        with col3:
            Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase')


        with col1:
            Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase')

        with col2:
            Total_Protiens = st.text_input('Total Protiens')

        with col3:
            Albumin = st.text_input('Albumin')


        with col1:
            Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio')  
        

        liver_diagnosis = ''

        if st.button('Liver Disease Test Result'):


            user_input = [Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]

            user_input = [float(x) for x in user_input]

            liver_prediction = model.predict([user_input])

            if liver_prediction[0] == 1:
                liver_diagnosis = 'The person is having liver disease'
            else:
                liver_diagnosis = 'The person does not have any liver disease'

        st.success(liver_diagnosis)

def predict_asthma_disease(model):
        
    col1, col2, col3 = st.columns(3)
        
    with col1:
        Tiredness = st.text_input('Tiredness')
        
    with col2:
        Dry_Cough = st.text_input('Dry-Cough')
    
    with col3:
        Difficulty_in_Breathing = st.text_input('Difficulty in Breathing')

    with col1:
        Sour_throat = st.text_input('Sore-throat') 

    with col2:
        None_Sympton = st.text_input('None_Symptom')

    with col3:
        Pains = st.text_input('Pains')

    with col1:
        Nasal_Congestion = st.text_input('Nasal-Congestion')

    with col2:
        Runny_Nose = st.text_input('Runny-Nose')

    with col3:
        None_Experiencing = st.text_input('None-Experiencing')

    with col1:
        Age_0_9 = st.text_input('Age_0-9')

    with col2:
        Age_10_19 = st.text_input('Age_10-19')

    with col3:
        Age_20_24 = st.text_input('Age_20-24')

    with col1:
        Age_25_59 = st.text_input('Age_25-59')

    with col2:
        Age_60 = st.text_input('Age_60')

    with col3:
        Gender_Female= st.text_input('Gender_Female')

    with col1:
        Gender_Male= st.text_input('Gender_Male')

    with col2:
        Severity_Mild= st.text_input('Severity_Mild')

    with col3:
        Severity_Moderate= st.text_input('Severity_Moderate')

    asthma_diagnosis = ''

    if st.button('Asthma Disease Test Result'):
        user_input = [Tiredness, Dry_Cough, Difficulty_in_Breathing, Sour_throat, None_Sympton, Pains, Nasal_Congestion, Runny_Nose, None_Experiencing, 
                      Age_0_9, Age_10_19, Age_20_24, Age_25_59, Age_60, Gender_Female, Gender_Male, Severity_Mild, Severity_Moderate]
                
        user_input = [float(x) for x in user_input]
        user_input=np.asarray(user_input)

        user_input=user_input.reshape(1,-1)

        asthma_prediction = model.predict(user_input)

        if asthma_prediction[0] == 1:
            asthma_diagnosis = 'The person is having asthma disease'
        else:
            asthma_diagnosis = 'The person is having asthma disease'

    st.success(asthma_diagnosis)

def display_diabetes_faq():
    with st.sidebar.expander("Diabetes FAQ"):
        diabetes_faqs = {
            "Diabetes FAQ":"FAQs below regarding diabetes.",
            "What is diabetes?": "Diabetes is a chronic disease that occurs when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar.",
            "What are the symptoms of diabetes?": "Symptoms of diabetes include frequent urination, increased thirst, unexplained weight loss, extreme hunger, fatigue, blurred vision, and slow healing of wounds.",
            "What values should I input for Insulin Level?": "Enter the insulin level given on your report in IU/ml (International Units per milliliter).",
            "What values should I input for BMI?": "Enter the BMI value. BMI is calculated as weight (kg) divided by height squared (m^2).",
            "What values should I input for Diabetes Pedigree Function(DPF)?": "DPF = Σ(0.1 × history), where Σ represents summation, and history represents the degree of relationship for each relative with diabetes(coded 1 for 1st-degree relatives, 0.5 for 2nd-degree relatives, and 0.25 for 3rd-degree relatives).",
            "What should I do in case of a diabetic emergency?": "In case of a diabetic emergency such as hypoglycemia (low blood sugar) or hyperglycemia (high blood sugar), it is important to take appropriate action. For hypoglycemia, consume sugary foods or drinks to raise blood sugar levels. For hyperglycemia, monitor blood sugar levels closely, drink plenty of water, and seek medical attention (call 108 or 112 (India)) .",
            "What are the signs of a diabetic emergency?": "Signs of a diabetic emergency include dizziness, confusion, sweating, trembling, weakness, extreme thirst, frequent urination, nausea, vomiting, abdominal pain, fruity-smelling breath (in case of hyperglycemia), and unconsciousness.",
        }

        display_faq(diabetes_faqs)

def display_heart_disease_faq():
    with st.sidebar.expander("Heart Disease FAQ"):
        heart_disease_faqs = {
            "Heart Disease FAQs":"FAQs below regarding heart diseases.",
            "What are the risk factors for heart disease?": "Risk factors for heart disease include high blood pressure, high cholesterol, smoking, diabetes, obesity, poor diet, physical inactivity, and excessive alcohol consumption.",
            "How is heart disease diagnosed?": "Heart disease is diagnosed through various tests such as electrocardiogram (ECG), echocardiogram, stress tests, blood tests, and coronary angiography.",
            "What values should I input for Serum Cholestoral?": "Enter the total serum cholestoral value in mg/dL (in your lipid profile report).",
            "What values should I input for Resting Electrocardiographic Results?": "It is written at top of your ECG (the wavy one :)) report (put normal if Normal Sinus Rythm is written).",
            "What values should I input for ST depression induced by exercise?": "When entering this value, provide the magnitude of ST segment depression (in mm) observed during exercise testing. If no ST segment depression is observed, enter 0.",
            "What values should I input for Number of Major Vessels Colored by Flourosopy?": "When entering this value, provide the number of major vessels (0-3) that appear to have significant narrowing or blockages as observed during the cardiac examination.",
            "What values should I input for Thal?": "Thal refers to thallium stress testing, which is a type of nuclear imaging test used to evaluate blood flow to the heart muscle.(If not done, put normal as its rare.)",
            "What are the signs of a heart attack?": "Common signs of a heart attack include chest discomfort or pain (often described as pressure, tightness, or squeezing), shortness of breath, nausea or vomiting, lightheadedness or dizziness, discomfort in the arms, back, neck, jaw, or stomach, and cold sweats. Not everyone experiences these symptoms, and they can vary between individuals.",
            "What should I do during a heart attack?": "During a heart attack, it's crucial to act quickly. Call emergency services immediately (108 or 112 (India) or your local emergency number). While waiting for help, chew and swallow aspirin (if available) to help reduce blood clotting. Stay calm, and if you have been prescribed nitroglycerin, take it as directed. If you are experiencing chest pain, sit down and rest in a comfortable position. Avoid exertion or stress.",
            "What should I do if someone is having a heart attack?": "If you suspect someone is having a heart attack, call emergency services immediately (108 or 112 (India) or your local emergency number). Encourage the person to sit down and rest in a comfortable position. If they have been prescribed nitroglycerin/sorbitol, assist them in taking it as directed. Stay with the person and monitor their condition while waiting for help to arrive.",
            # Add more FAQs specific to heart disease
        }

        display_faq(heart_disease_faqs)

def display_parkinsons_faq():
    with st.sidebar.expander("Parkinson's FAQ"):
        parkinsons_faqs = {
            "Parkinson's disease FAQs":"FAQs below regarding Parkinson's disease.",
            "What is Parkinson's disease?": "Parkinson's disease is a neurodegenerative disorder that affects movement. It is characterized by tremors, stiffness, slow movements, and impaired balance and coordination.",
            "What are the treatments for Parkinson's disease?": "Treatments for Parkinson's disease include medications, deep brain stimulation (DBS), physical therapy, and lifestyle modifications.",
             "What should I do if I experience sudden and severe symptoms of Parkinson's disease?": "If you experience sudden and severe symptoms such as difficulty breathing, chest pain, severe tremors, or loss of consciousness, seek emergency medical attention immediately. Call emergency services (108 (India) or your local emergency number) or go to the nearest emergency room.",
            "What should I do if I fall and injure myself due to Parkinson's symptoms?": "If you fall and injure yourself due to symptoms such as muscle stiffness, tremors, or balance problems, assess the severity of your injury. If you are unable to get up or if you suspect a serious injury such as a fracture or head injury, seek medical attention immediately. If the injury is minor, try to safely get up and rest.",
            "What should I do if I experience difficulty swallowing or choking episodes?": "If you experience difficulty swallowing or choking episodes, remain calm and try to cough to clear your airway. If you are unable to clear your airway or if you are experiencing severe difficulty breathing, seek immediate medical attention. Call emergency services (108 (India) or your local emergency number) for assistance.",
            "What is Fo(Hz), Fhi(Hz) and Flo(Hz)?": "These are fundamental, highest and lowest frequency of voice in Hertz.",
            "What values should I input for MDVP:Jitter(%)?": "Enter the MDVP:Jitter(%) value.",
            "What is Jitter(Abs) vs Jitter(%)?": "Absolute jitter in microseconds and percentage jitter.",
            "What values should I input for MDVP_RAP?": "Enter the relative average perturbation. This measures the average absolute difference between consecutive periods.",
            "What values should I input for MDVP_PPQ?": "Enter the five-point period perturbation quotient. This measures the average absolute difference between consecutive periods normalized by dividing by the period.",
            "What values should I input for Jitter_DDP?": "Enter the average absolute difference of differences between consecutive periods. This is double the value of MDVP_RAP.",
            "What values should I input for MDVP_Shimmer?": "Enter the variation in amplitude of the voice signal. This measures the peak-to-peak variation in amplitude.",
            "What values should I input for MDVP_Shimmer(dB)?": "Enter the variation in amplitude of the voice signal in decibels (dB). This measures the peak-to-peak variation in amplitude in decibels.",
            "What values should I input for Shimmer_APQ3?": "Enter the three-point amplitude perturbation quotient. This measures the average absolute difference between consecutive periods normalized by dividing by the amplitude.",
            "What values should I input for Shimmer_APQ5?": "Enter the five-point amplitude perturbation quotient. This measures the average absolute difference between consecutive periods normalized by dividing by the amplitude.",
            "What values should I input for MDVP_APQ?": "Enter the overall amplitude perturbation quotient. This is the average of Shimmer_APQ3 and Shimmer_APQ5.",
            "What values should I input for Shimmer_DDA?": "Enter the average absolute difference between consecutive periods, measured in milliseconds.",
            "What values should I input for NHR?": "Enter the noise-to-harmonics ratio. This is the ratio of the noise component to the harmonic component of the voice signal.",
            "What values should I input for HNR?": "Enter the harmonics-to-noise ratio. This is the ratio of the harmonic component to the noise component of the voice signal.",
            "What values should I input for RPDE?": "Enter the recurrence period density entropy. This is a measure of the complexity of the voice signal.",
            "What values should I input for DFA?": "Enter the detrended fluctuation analysis. This is a measure of the self-similarity of the voice signal.",
            "What values should I input for spread1?": "Enter the nonlinear measure of fundamental frequency variation.",
            "What values should I input for spread2?": "Enter the nonlinear measure of fundamental frequency variation.",
            "What values should I input for D2?": "Enter the nonlinear measure of fundamental frequency variation.",
            "What values should I input for PPE?": "Enter the Pitch Period Entropy. This is a measure of the signal's periodicity."
            # Add more FAQs specific to Parkinson's disease
        }

        display_faq(parkinsons_faqs)

def display_liver_disease_faq():
    with st.sidebar.expander("Liver Disease FAQ"):
        liver_disease_faqs = {
            "Liver Disease FAQs":"FAQs below regarding liver diseases.",
            "What are the common symptoms of liver disease?": "Common symptoms of liver disease include jaundice (yellowing of the skin and eyes), abdominal pain and swelling, nausea, vomiting, fatigue, dark urine, pale stools, and unexplained weight loss.",
            "What are the causes of liver disease?": "Liver disease can be caused by various factors, including viral infections (such as hepatitis B and C), excessive alcohol consumption, non-alcoholic fatty liver disease (NAFLD), autoimmune conditions, genetic disorders, and certain medications and toxins.",
            "What are the risk factors for liver disease?": "Risk factors for liver disease include excessive alcohol consumption, obesity, diabetes, exposure to certain toxins and chemicals, and a family history of liver disease.",
            "How is liver disease diagnosed?": "Liver disease is diagnosed through various tests, including blood tests to assess liver function, imaging tests (such as ultrasound, CT scan, or MRI), and liver biopsy.",
            "What values should I input for Total Bilirubin and Direct Bilirubin?": "Enter the total bilirubin and direct bilirubin values from your blood test report in mg/dL.",
            "What values should I input for Alkaline Phosphotase, Alamine Aminotransferase, and Aspartate Aminotransferase?": "Enter the levels of alkaline phosphatase (ALP), alanine aminotransferase (ALT), and aspartate aminotransferase (AST) from your liver function test report.",
            "What are the treatments for liver disease?": "Treatment for liver disease depends on the underlying cause and may include lifestyle changes (such as avoiding alcohol and maintaining a healthy diet), medications, and in some cases, liver transplantation.",
            "What should I do if I suspect I have liver disease?": "If you experience symptoms of liver disease or have risk factors for liver disease, it is important to consult a healthcare professional for evaluation and diagnosis. They can perform the necessary tests to determine the cause of your symptoms and recommend appropriate treatment.",
        }

        display_faq(liver_disease_faqs)

def display_asthma_disease_faq():
    with st.sidebar.expander("Asthma Disease FAQ"):
        asthma_disease_faqs = {
            "Asthma Disease FAQs":"FAQs below regarding asthma.",
            "What is asthma?": "Asthma is a chronic respiratory condition characterized by inflammation and narrowing of the airways, resulting in symptoms such as wheezing, coughing, shortness of breath, and chest tightness.",
            "What are the common triggers for asthma attacks?": "Common triggers for asthma attacks include allergens (such as pollen, dust mites, and pet dander), respiratory infections, exercise, cold air, air pollution, tobacco smoke, and certain medications.",
            "What are the different types of asthma?": "Asthma can be classified into several types, including allergic asthma, non-allergic asthma, exercise-induced asthma, occupational asthma (triggered by workplace exposures), and aspirin-exacerbated respiratory disease (AERD).",
            "How is asthma diagnosed?": "Asthma is diagnosed based on medical history, physical examination, lung function tests (such as spirometry), and sometimes allergy testing.",
            "What values should I input for Tiredness, Dry-Cough, Sour-throat, etc.?": "For symptoms, enter 1 if you experience the symptom and 0 if you do not experience it.",
            "What should I do during an asthma attack?": "During an asthma attack, it's important to remain calm and follow your asthma action plan. Use your rescue inhaler as prescribed, sit upright, and try to relax your breathing. If symptoms worsen or do not improve with medication, seek emergency medical attention.",
            "How can asthma be managed?": "Asthma can be managed with a combination of medication (such as bronchodilators and corticosteroids), avoiding triggers, maintaining a healthy lifestyle, and following an asthma action plan developed with your healthcare provider.",
            "Can asthma be cured?": "While asthma cannot be cured, it can be effectively managed with proper treatment and lifestyle modifications. Most people with asthma are able to lead active and fulfilling lives with appropriate management.",
            "What should I do if I suspect I have asthma?": "If you experience symptoms of asthma, such as recurrent wheezing, coughing, or shortness of breath, it is important to consult a healthcare professional for evaluation and diagnosis. They can perform tests to determine if asthma is the cause of your symptoms and develop a treatment plan tailored to your needs.",
        }

        display_faq(asthma_disease_faqs)

def display_faq(faqs):
    for question, answer in faqs.items():
        with st.sidebar.expander(question):
            st.write(answer)
                                                      

if __name__ == "__main__":
  main()
