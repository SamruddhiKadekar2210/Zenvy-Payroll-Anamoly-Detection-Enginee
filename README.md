Project Overview

This project implements a Payroll Anomaly Detection Engine using unsupervised learning to identify fraudulent or abnormal payroll activities such as:

Salary manipulation

Fake or excessive overtime claims

The system works without labeled data, supports batch training and real-time inference, and is designed to handle concept drift.

Problem Statement

Design and implement an anomaly detection engine that:

Uses unsupervised learning

Detects payroll anomalies (salary & overtime fraud)

Handles concept drift

Supports both batch and real-time pipelines

Technologies Used

Python

Scikit-learn

FastAPI

Uvicorn

NumPy / Pandas

Joblib

 Algorithm Selection Rationale
Isolation Forest (Unsupervised)

Isolation Forest is chosen because:

It works without labeled data

Efficiently isolates anomalies

Scales well to large datasets

Widely used in real-world fraud detection systems

Anomalies are detected based on how easily a data point can be isolated compared to normal points.

 Features Used for Detection

Salary change percentage

Salary deviation from peer average

Overtime ratio (overtime / total hours)

Overtime deviation from peer average

 System Architecture
Batch Pipeline
data_generator.py → data.csv → batch.py → model.joblib

Real-Time Pipeline
Client → FastAPI (/predict) → Isolation Forest → Anomaly Score

🧪 Pseudocode
Generate payroll data
Extract relevant features
Train Isolation Forest model
Save trained model

For each incoming payroll record:
    Extract features
    Compute anomaly score
    If score > threshold:
        Flag as anomaly

 Evaluation Strategy (Without Labels)

Since labeled data is not available, the model is evaluated using the following unsupervised techniques:

1. Anomaly Score Distribution

Analyze the distribution of anomaly scores

Extreme values indicate abnormal payroll behavior

2. Threshold-Based Detection

A predefined anomaly threshold is used

Records above the threshold are flagged as anomalies

3. Temporal Stability

Monitor anomaly rates over time

Sudden changes indicate concept drift

Batch retraining helps adapt to new patterns

4. Manual Validation (Optional)

Flagged anomalies can be reviewed by HR or finance teams

Feedback can guide future improvements

Deployment Plan
1. Local Deployment

Install required Python packages

Train model using batch pipeline

Start FastAPI server using Uvicorn

Access API at http://127.0.0.1:8000

2. Real-Time Inference

FastAPI loads the trained model (model.joblib)

Incoming payroll records are processed via /predict

Anomaly score and decision returned instantly

3. Batch Retraining (Concept Drift Handling)

Periodically retrain model using updated payroll data

Replace old model with newly trained model

Keeps system adaptive to changing trends

4. Production Deployment (Optional)

Dockerize the application

Deploy on cloud platforms (AWS / Azure / GCP)

Integrate CI/CD pipeline for automated updates

 API Details
Endpoint
POST /predict

Sample Request
{
  "salary": 90000,
  "prev_salary": 50000,
  "overtime_hours": 40,
  "total_hours": 160,
  "peer_stats": {
    "avg_salary": 52000,
    "avg_overtime": 12
  }
}

Sample Response
{
  "anomaly_score": 0.82,
  "is_anomaly": true
}

 How to Run the Project
pip install -r requirements.txt
python data_generator.py
python batch.py
uvicorn realtime:app --reload

 Project Structure
anomaly_detection_engine/
├── batch.py
├── realtime.py
├── model.py
├── features.py
├── config.py
├── data_generator.py
├── data.csv
├── model.joblib
├── README.md
