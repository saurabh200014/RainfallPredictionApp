import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
def show_predict_page():
    st.title("Rainfall Prediction")

    st.write("""### We need some information to predict the rainfall""")
    precipitation = st.slider("Precipitation", 0, 56, 1)
    temp_min = st.slider("Minimum Temperature", -8, 19, 1)
    temp_max = st.slider("Maximum Temperature", -2, 36, 1)
    wind = st.slider("Wind speed", 0, 10, 1)


    ok = st.button("Calculate Rainfall %")
    if ok:
        X = np.array([[precipitation, temp_min, temp_max, wind]])
        X = X.astype(float)

        weather = regressor.predict(X)
        # st.subheader(f"The estimated chance of rainfall is ${weather[0]:.2f}")
        if (weather[0]/3)>1:
            st.subheader(f"There will be sunny weather")
        else:
            st.subheader(f"There will be rainfall")

        