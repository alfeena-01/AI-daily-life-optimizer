import pandas as pd
from prophet import Prophet

def forecast_activity(data, column="sleep_hours", periods=7):
    """
    Forecasts future values for a given activity column using Prophet.
    """
    if column not in data.columns or len(data) < 3:
        return None, "Not enough data to forecast yet."

    # Clean data
    df = data[["date", column]].dropna()
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna().rename(columns={"date": "ds", column: "y"})

    # Safety checks
    if df["ds"].nunique() < 3:
        return None, "Not enough unique dates to forecast."
    if df["y"].nunique() < 2:
        return None, "Data has no variation, cannot forecast."

    # Forecast
    try:
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        return forecast, f"Forecast generated for {column}."
    except Exception as e:
        return None, f"Forecasting failed: {e}"
