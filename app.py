import streamlit as st
import pandas as pd
import datetime
from utils.suggestion_engine import generate_suggestion
from utils.weather_api import get_weather
from utils.health_api import get_google_fit_data
from utils.sensors import get_manual_input
from utils.pattern_detection import detect_focus_patterns
from utils.forecasting import forecast_activity
from utils.db_manager import init_db, insert_activity, get_all_activity
from utils.ml_models import train_step_predictor, cluster_focus_patterns
from utils.suggestion_engine import generate_suggestion, generate_daily_tip
# Elegant UI Theme
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Glassmorphism cards */
    .card {
        background: rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease-in-out;
    }

    /* Hover effect for 3D feel */
    .card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 30px rgba(0,0,0,0.6);
    }

    /* Headings with glow */
    h1, h2, h3 {
        color: #f5f5f5;
        text-shadow: 0 0 10px rgba(0,255,255,0.7);
    }
    </style>
""", unsafe_allow_html=True)


from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Example working animation
lottie_focus = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q5pk6p1k.json")

if lottie_focus:
    st_lottie(lottie_focus, height=200, key="focus")
else:
    st.warning("⚠️ Could not load animation.")






st.title("🌟 AI Daily Life Optimizer")

# Weather
st.subheader("🌤 Current Weather")
st.write(get_weather("Tirur"))

# Google Fit Data (mock for now)
st.subheader("🏃 Google Fit Data")
fit_data = get_google_fit_data()
st.write(fit_data)

# Initialize DB
init_db()

# Manual Input
st.subheader("✍️ Manual Input")
manual_data = get_manual_input()
selected_date = st.date_input("Select date", datetime.date.today())
manual_data["date"] = selected_date

if st.button("Save today's log"):
    insert_activity(
        manual_data["date"],
        manual_data["sleep_hours"],
        manual_data["steps"],
        manual_data["screen_time"]
    )
    st.success("Data saved successfully!")

# Load full dataset
data = get_all_activity()
st.subheader("📊 Your Activity Data")
st.write(data)

# Train ML model
ml_model, msg = train_step_predictor(data)
st.info(msg)

# Forecasts
forecasts = {}
for col in ["sleep_hours", "steps", "screen_time"]:
    forecast, msg = forecast_activity(data, col)
    st.subheader(f"🔮 {col.replace('_',' ').title()} Forecast")
    if forecast is None:
        st.warning(msg)
    else:
        st.line_chart(forecast[["ds", "yhat"]].set_index("ds"))
        forecasts[col] = forecast.iloc[-1]["yhat"]

# Suggestion
suggestion = generate_suggestion(data, datetime.date.today(), forecasts, ml_model)
st.subheader("💡 Today's Suggestion")
st.success(suggestion)

# Focus Patterns
clustered_data, msg = cluster_focus_patterns(data)
st.subheader("🧠 Focus Pattern Analysis")
st.info(msg)

if clustered_data is not None:
    # Map cluster numbers to human-friendly labels
    cluster_labels = {
        0: "Balanced Day",
        1: "Low-Energy Day",
        2: "Mixed Day",
        3: "High Screen Day"
    }

    # Add descriptive explanations
    cluster_explanations = {
        "Balanced Day": "Best time for deep work and important tasks.",
        "Low-Energy Day": "Avoid heavy tasks, focus on rest and light routines.",
        "Mixed Day": "Moderate productivity — plan balanced tasks.",
        "High Screen Day": "Too much screen time — take breaks to protect focus."
    }

    # Attach labels to the clustered data
    clustered_data["pattern_name"] = clustered_data["cluster"].map(cluster_labels)

    # 1️⃣ Cluster Distribution Chart
    st.subheader("📊 Focus Pattern Distribution")
    cluster_counts = clustered_data["pattern_name"].value_counts()
    st.bar_chart(cluster_counts)

    # 2️⃣ Timeline Visualization
    st.subheader("📅 Focus Pattern Timeline")
    st.line_chart(clustered_data.set_index("date")["cluster"])

    # 3️⃣ Interactive 3D Chart
    import plotly.express as px
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 Focus Pattern Distribution (3D)")
    fig = px.scatter_3d(clustered_data,
                    x="sleep_hours",
                    y="steps",
                    z="screen_time",
                    color="pattern_name",
                    size="steps",
                    symbol="pattern_name",
                    title="Focus Patterns in 3D Space")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4️⃣ Daily Focus Card
    today_pattern = clustered_data.iloc[-1]["pattern_name"]
    st.subheader("📌 Today's Focus Pattern")
    st.success(f"Your day matches: {today_pattern}")
    st.caption(cluster_explanations[today_pattern])


    # Show history of patterns
    st.subheader("📅 Past Focus Patterns")
    for _, row in clustered_data.iterrows():
        st.markdown(f"**{row['date']} → {row['pattern_name']}**")

# Daily Tip Card
today_pattern = clustered_data.iloc[-1]["pattern_name"] 
if clustered_data is not None :
   st.markdown('<div class="card">', unsafe_allow_html=True)
   st.subheader("📌 Today's Focus Pattern")
   st.write(f"{today_pattern} — {cluster_explanations[today_pattern]}")
   st.markdown('</div>', unsafe_allow_html=True)

else :None

weather_info = get_weather("Tirur")

daily_tip = generate_daily_tip(data, forecasts, today_pattern, weather_info)
st.subheader("💡 Daily Tip")
st.info(daily_tip)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("💡 Daily Tip")
st.write(daily_tip)
st.markdown('</div>', unsafe_allow_html=True)

