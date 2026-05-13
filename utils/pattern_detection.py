import pandas as pd
from sklearn.cluster import KMeans

def detect_focus_patterns(data):
    """
    Detects clusters in activity data (sleep, steps, screen time)
    to find best focus times.
    """
    if data.empty:
        return "No data available yet."

    # If fewer than 2 samples, skip clustering
    if len(data) < 2:
        return "Not enough data yet. Add more activity records to detect patterns."

    # Use only numeric features
    features = data[["sleep_hours", "steps", "screen_time"]]

    # Simple clustering
    kmeans = KMeans(n_clusters=2, random_state=42)
    kmeans.fit(features)

    # Find which cluster is 'better' (higher sleep + steps, lower screen time)
    cluster_means = features.groupby(kmeans.labels_).mean()
    cluster_means["score"] = cluster_means["sleep_hours"] + cluster_means["steps"] - cluster_means["screen_time"]
    best_cluster = cluster_means["score"].idxmax()

    return f"Your best focus pattern matches cluster {best_cluster}. Try working during those times."
