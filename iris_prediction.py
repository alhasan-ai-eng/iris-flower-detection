import streamlit as st
import pickle

st.title("Iris Prediction")
sl=st.number_input("Enter Sepal - Length")
sw=st.number_input("Enter Sepal - Width")
pl=st.number_input("Enter Petal - Length")
pw=st.number_input("Enter Petal - Width")

btn=st.button("Predict!")

if btn:
    y_pred=pickle.load(open("iris.pkl","rb"))
    res=y_pred.predict([[sl,sw,pl,pw]])[0]


    st.markdown(f"Result: {res}")