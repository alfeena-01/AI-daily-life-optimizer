import random

def generate_suggestion(data, today, forecasts=None, ml_model=None):
    if data.empty:
        return "No activity data yet. Log your sleep, steps, and screen time to get suggestions."

    sleep = data["sleep_hours"].mean() if "sleep_hours" in data else 0
    steps = data["steps"].mean() if "steps" in data else 0
    screen = data["screen_time"].mean() if "screen_time" in data else 0

    # Forecast-aware suggestions
    if forecasts:
        tomorrow_sleep = forecasts.get("sleep_hours")
        tomorrow_steps = forecasts.get("steps")
        tomorrow_screen = forecasts.get("screen_time")

        if tomorrow_sleep and tomorrow_sleep < 7:
            return "Forecast shows less than 7 hours of sleep tomorrow. Plan an early bedtime tonight."
        if tomorrow_steps and tomorrow_steps < 5000:
            return "Forecast predicts low steps tomorrow. Schedule a walk to stay active."
        if tomorrow_screen and tomorrow_screen > 6:
            return "Forecast shows high screen time tomorrow. Try a digital detox in the evening."

    # ML-based suggestion
    if ml_model:
        last_row = data.iloc[-1]
        predicted_steps = ml_model.predict([[last_row["sleep_hours"], last_row["screen_time"]]])[0]
        if predicted_steps < 6000:
            return "ML predicts low activity tomorrow. Add a short workout to your plan."

    # Past-data suggestions
    if sleep < 7:
        return "You slept less than 7 hours on average. Try to rest earlier tonight."
    elif steps < 5000:
        return "Your step count is low. A short walk today could boost your energy."
    elif screen > 6:
        return "Your screen time is high. Consider a short digital detox this evening."
    else:
        return "Great balance today! Keep up the healthy routine."

def generate_daily_tip(data, forecasts=None, focus_pattern=None, weather=None):
    tips = []

    # Focus pattern tip
    if focus_pattern == "Balanced Day":
        tips.append("You were most focused yesterday. Try reviewing notes at the same time today.")
    elif focus_pattern == "Low-Energy Day":
        tips.append("Energy is low — schedule lighter tasks and rest breaks.")
    elif focus_pattern == "Mixed Day":
        tips.append("Moderate productivity — plan balanced tasks.")
    elif focus_pattern == "High Screen Day":
        tips.append("Too much screen time — take breaks to protect focus.")

    # Weather tip
    if weather:
        if "sunny" in weather.lower():
            tips.append("Weather is sunny — air-dry clothes today to save energy.")
        elif "rain" in weather.lower():
            tips.append("Rainy day — plan indoor stretching or reading.")

    # Sleep tip
    if not data.empty:
        last_sleep = data.iloc[-1]["sleep_hours"]
        if last_sleep < 7:
            tips.append(f"You slept only {last_sleep:.1f} hours. Aim for a short nap this afternoon.")

    # Forecast tip
    if forecasts:
        tomorrow_steps = forecasts.get("steps")
        if tomorrow_steps and tomorrow_steps < 5000:
            tips.append("Forecast predicts low steps tomorrow. Schedule a walk to stay active.")

    # Return combined tips as bullet points
    if tips:
        return "\n".join([f"- {t}" for t in tips])
    else:
        return "Keep up the good work!"
