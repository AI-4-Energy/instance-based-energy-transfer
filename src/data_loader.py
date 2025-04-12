import os
import pandas as pd

def load_environmental_data(data_path):
    """Load weather and carbon intensity data."""
    weather = pd.read_csv(os.path.join(data_path, "weather.csv"))
    carbon = pd.read_csv(os.path.join(data_path, "carbon_intensity.csv"))
    env_data = pd.concat([weather, carbon], axis=1)
    return env_data
