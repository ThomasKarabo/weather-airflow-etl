from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import os

def fetch_weather_data():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.6895,  # Example: Tokyo latitude
        "longitude": 139.6917,  # Example: Tokyo longitude
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract relevant data
    weather_data = {
        "temperature": data["current_weather"]["temperature"],
        "windspeed": data["current_weather"]["windspeed"],
        "weathercode": data["current_weather"]["weathercode"],
        "time": data["current_weather"]["time"]
    }
    
    # Save to CSV
    df = pd.DataFrame([weather_data])
    output_file = os.path.join(os.getcwd(), 'weather_data.csv')
    df.to_csv(output_file, index=False)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'weather_to_csv',
    default_args=default_args,
    description='A simple DAG to fetch weather data and save to CSV',
    schedule_interval='30 9 * * 1-5',  # Every weekday at 09:30
    catchup=False,
) as dag:

    fetch_weather = PythonOperator(
        task_id='fetch_weather',
        python_callable=fetch_weather_data,
    )

    fetch_weather