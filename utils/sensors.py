import streamlit as st

def get_manual_input():
    sleep_hours = st.number_input("Enter last night's sleep hours:", min_value=0.0, max_value=24.0, step=0.5)
    steps = st.number_input("Enter today's step count:", min_value=0, step=100)
    screen_time = st.number_input("Enter today's screen time (hours):", min_value=0.0, max_value=24.0, step=0.5)
    return {"sleep_hours": sleep_hours, "steps": steps, "screen_time": screen_time}
