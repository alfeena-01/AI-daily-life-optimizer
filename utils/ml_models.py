import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

def train_step_predictor(data):
    """Predict steps based on sleep and screen time."""
    if len(data) < 5:
        return None, "Not enough data to train model."
    X = data[["sleep_hours", "screen_time"]]
    y = data["steps"]
    model = LinearRegression().fit(X, y)
    return model, "Step predictor trained."

def predict_steps(model, sleep_hours, screen_time):
    return int(model.predict([[sleep_hours, screen_time]])[0])

def cluster_focus_patterns(data, n_clusters=3):
    """Cluster days into focus patterns based on sleep, steps, screen time."""
    if len(data) < n_clusters:
        return None, "Not enough data to cluster."
    X = data[["sleep_hours", "steps", "screen_time"]]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    data["cluster"] = kmeans.labels_
    return data, "Focus patterns clustered."
