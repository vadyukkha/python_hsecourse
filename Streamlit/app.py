import numpy as np
import pandas as pd
import streamlit as st

st.title("Приложение на Streamlit")

user_input = st.text_input("Введите текст:", "")

if st.button("Показать текст"):
    st.write(f"Вы ввели: {user_input}")

number = st.slider("Выберите число:", min_value=0, max_value=100, value=50)
st.write(f"Выбранное число: {number}")

data = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])

st.line_chart(data)
