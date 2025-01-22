# twitter-airflow-S3-pipeline

# Twitter Data Pipeline

## Overview
This project demonstrates a simple data pipeline that fetches tweets from the Twitter API and stores them as a CSV file in an Amazon S3 bucket. The pipeline is orchestrated using Apache Airflow, which was deployed and tested on an Amazon EC2 instance, and leverages Python scripts for data extraction and processing.

## Features
- Fetch tweets from the Twitter API using Tweepy.
- Save tweets as a CSV file in an AWS S3 bucket.
- Automate the process using Apache Airflow.
- Handle rate limits and errors gracefully.

## Project Structure
```plaintext
twitter_pipeline/
├── dags/
│   ├── twitter_dag.py        # Airflow DAG script to orchestrate the pipeline
├── scripts/
│   ├── twitter_etl.py        # Python script for fetching and processing tweets
├── requirements.txt          # List of required Python packages
├── README.md                 # Project documentation
```
## Prerequisites
To run this project, you need the following:
- **Python 3.8 or higher**
- **Apache Airflow** installed and configured.
- **AWS Account** with an S3 bucket for storing the data.
- **Twitter Developer Account** for API access (bearer token).

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/twitter-pipeline.git
cd twitter-pipeline
```
### 2. Set Up Python Environment
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Configure AWS and Twitter Credentials
Update your credentials in the `twitter_etl.py` script:
- Replace `bearer_token` with your Twitter API bearer token.
- Configure your AWS S3 bucket name in the `fetch_user_tweets` function.

### 4. Set Up Airflow on EC2
- Launch an Amazon EC2 instance (e.g., `t2.micro` for testing purposes).
- Install and configure Apache Airflow on the EC2 instance.
- Add the `twitter_dag.py` file to the `dags` folder of your Airflow installation.

### 5. Run Airflow
Start the Airflow scheduler and webserver on your EC2 instance:
```bash
airflow scheduler &
airflow webserver -p 8080 &
```
Access the Airflow UI at `http://<EC2-public-IP>:8080` and trigger the `twitter_dag` DAG.

## Usage
Trigger the Airflow DAG from the Airflow UI or CLI.  
The DAG will fetch tweets from the specified Twitter username and save them as a CSV file in the configured S3 bucket.

## Example Output
The pipeline generates a CSV file in your S3 bucket with the following structure:
```plaintext
user,tweet,created_at,likes,retweets
elonmusk,"Tweet text",2025-01-01 12:00:00,1234,567
...
```
## Future Improvements
- Replace SQLite with PostgreSQL for better Airflow performance.
- Implement transformations before saving data to S3.
- Integrate with AWS Redshift for analytics.
- Add monitoring and alerting for the pipeline.






