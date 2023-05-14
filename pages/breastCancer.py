import tensorflow as tf
import streamlit as st
import numpy as np
import cv2
from twilio.rest import Client
import os

model_path = "./breastCancerClassifier.h5"

@st.cache_resource
def load_model():
    try:
        with tf.device('/cpu:0'): 
            model = tf.keras.models.load_model(model_path, compile=False)
            return model 
    except (FileNotFoundError, RuntimeError) as e:
        st.error(str(e))
        return None

def model_pred(img, model):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (224, 224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        with tf.device('/cpu:0'):
            pred = model.predict(img)

        return pred[0][0]

    except (cv2.error, RuntimeError) as e:
        st.error(str(e))
        return None

def send_result_to_patient(result, phone_number):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_PHONE_NUMBER']

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Dear Patient: Following your visit to our Hospital, "
             f"Here is your result of the Image Diagnosis: {result}",
        from_=twilio_number,
        to=phone_number
    )
    return message.sid

def main():
    st.title("Breast Cancer Image Diagnostic (Benign / Malignant)")
    result = ""
    img_file = st.file_uploader("Please Upload Patient's Mammogram Image", type=["png", "jpeg"])
    
    if img_file is not None:
        img = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), 1)
        st.image(img, caption="Uploaded image", use_column_width=True)
        
        # Press this button to see results
        if st.button("See Results"):
            pred = model_pred(img, model)
            if pred is not None:
                if pred > 0.5:
                    result = "The Image Result is Malignant!"
                else:
                    result = "The Image Result is Benign!"
        
        st.success(result)  # Display the result
        
        if st.button('Share Results'):
            phone_number = st.text_input('Enter your Phone Number')
            if phone_number:
                message_sid = send_result_to_patient(result, phone_number)
                if message_sid:
                    st.success("Results shared successfully!")
                else:
                    st.error("Failed to send results. Please check your Twilio credentials and try again.")

model = load_model()

if model is not None:
    main()
