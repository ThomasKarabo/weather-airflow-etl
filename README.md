# Airflow Weather Project

This project is designed to extract today's weather data from the Open Meteo API and save it into a CSV file using Apache Airflow. The extraction process is automated to run daily on weekdays at 09:30.

## Project Structure

```
airflow-weather-project
├── dags
│   └── weather_to_csv_dag.py  # Contains the Airflow DAG definition
├── requirements.txt             # Lists the required Python dependencies
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   Clone this repository to your local machine.

2. **Install Dependencies**
   Navigate to the project directory and install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Apache Airflow**
   Ensure that Apache Airflow is installed and configured on your machine. You can follow the official Airflow documentation for installation instructions.

4. **Place the DAG File**
   Move the `weather_to_csv_dag.py` file into the `dags` folder of your Airflow installation.

5. **Start Airflow**
   Start the Airflow web server and scheduler:
   ```
   airflow webserver --port 8080
   airflow scheduler
   ```

6. **Access the Airflow UI**
   Open your web browser and go to `http://localhost:8080` to access the Airflow UI. You should see the DAG listed there.

7. **Trigger the DAG**
   You can manually trigger the DAG or wait for it to run automatically at the scheduled time.

## Additional Information

- The project uses the Open Meteo API to fetch weather data. Make sure to check their documentation for any usage limits or requirements.
- The output CSV file will be saved in the specified directory within the DAG configuration. Adjust the path as necessary in the `weather_to_csv_dag.py` file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.