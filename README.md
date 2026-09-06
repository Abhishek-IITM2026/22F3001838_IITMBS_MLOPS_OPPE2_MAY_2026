# 22F3001838_IITMBS_MLOPS_OPPE2_MAY_2026
# Heart Disease Prediction MLOps Pipeline
## IITM BS MLOPS OPPE-2 MAY 2026

**Roll Number:** 22F3001838  
**Repository:** 22F3001838_IITMBS_MLOPS_OPPE2_MAY_2026

---

# Objective

Build a production-ready, explainable, observable, scalable, and maintainable deployment for a Heart Disease Prediction Model using Google Cloud Platform (GCP).

The solution includes:

- Model Training
- Explainability using SHAP
- Fairness Testing using Fairlearn
- Dockerized FastAPI Deployment
- Kubernetes Deployment on GKE
- Horizontal Pod Autoscaling (Maximum 3 Pods)
- CI/CD using GitHub Actions
- Cloud Logging Observability
- Stress Testing using wrk
- Data Drift Detection

---

# Dataset

Heart Disease Dataset

Features:

- age
- gender
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

Target:

- yes
- no

Dataset Size:

- 303 rows
- 14 clinical features

---

# Repository Structure

```text
.
├── app.py
├── train.py
├── explainability.py
├── fairness.py
├── predict_100.py
├── drift.py
├── data.csv
├── sample_100.csv
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── hpa.yaml
├── models/
│   └── model.pkl
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

# Deliverable 1
## Private GitHub Repository

Repository created:

```text
22F3001838_IITMBS_MLOPS_OPPE2_MAY_2026
```

Collaborator added:

```text
IITMBSMLOps
```

---

# Deliverable 2
## Explainability using SHAP

Tool Used:

- SHAP

Generated:

```text
shap_summary.png
```

Observation:

Features appearing near the bottom of the SHAP summary plot have the least influence on the model prediction because their SHAP values remain close to zero across observations.

---

# Deliverable 3
## Fairness Testing

Tool Used:

- Fairlearn

Sensitive Attribute:

```text
age
```

Metric Used:

```text
Accuracy Score
```

Output generated using:

```bash
python fairness.py
```

The model performance was evaluated across different age groups.

---

# Deliverable 4
## Dockerized API Deployment on GKE

### API Framework

FastAPI

### Build Docker Image

```bash
docker build -t heart-api .
```

### Push Image

```bash
docker push us-central1-docker.pkg.dev/<PROJECT_ID>/heart-repo/heart-api:latest
```

### Kubernetes Resources

Deployment:

```yaml
deployment.yaml
```

Service:

```yaml
service.yaml
```

Autoscaling:

```yaml
hpa.yaml
```

### Horizontal Pod Autoscaler

```text
Min Pods : 1
Max Pods : 3
Target CPU : 50%
```

---

# Deliverable 5
## Logging & Observability

Tool Used:

- Google Cloud Logging

Prediction requests are logged with:

- Timestamp
- Input Features
- Predicted Output

Example:

```text
INPUT={...} PREDICTION=1
```

Cloud Logging Integration:

```python
import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()
```

Prediction requests generated using:

```bash
python predict_100.py
```

Generated:

```text
sample_100.csv
```

Total Predictions:

```text
100
```

---

# Deliverable 6
## Stress Testing

Tool Used:

```text
wrk
```

Command:

```bash
wrk -t12 -c2000 -d60s http://<EXTERNAL_IP>/
```

Results:

```text
Requests/sec: 783.24

Latency Avg: 608.10 ms

Total Requests:
47061

Socket Errors:
Read: 103
Write: 1
Timeout: 498
```

Analysis:

- API successfully handled more than 2000 concurrent connections.
- Throughput remained stable.
- Some timeout behavior was observed under heavy load.
- Kubernetes autoscaling can be used to improve performance under sustained traffic.

---

# Deliverable 7
## Input Drift Detection

Tool Used:

```text
scipy.stats.ks_2samp
```

Comparison:

```text
Training Dataset
vs
100 Prediction Samples
```

Result:

```text
No significant drift detected.
```

Example:

```text
age: No significant drift (p=0.4740)
chol: No significant drift (p=0.2883)
thalach: No significant drift (p=0.9588)
```

Conclusion:

The generated prediction data follows a similar distribution to the training dataset.

---

# CI/CD Pipeline

GitHub Actions Workflow:

```text
.github/workflows/ci.yml
```

Pipeline Stages:

1. Install Dependencies
2. Train Model
3. Run SHAP Explainability
4. Run Fairness Testing
5. Run Drift Detection
6. Build Docker Image
7. Push Image to Artifact Registry
8. Deploy to GKE
9. Apply HPA
10. Verify Deployment

---

# GCP Components Used

- Google Compute Engine
- Google Kubernetes Engine (GKE)
- Artifact Registry
- Cloud Logging
- GitHub Actions
- Workload Identity Federation

---

# API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "running"
}
```

### Prediction

```http
POST /predict
```

Example Request:

```json
{
  "age": 63,
  "gender": "male",
  "cp": 3,
  "trestbps": 145,
  "chol": 233,
  "fbs": 1,
  "restecg": 0,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 2.3,
  "slope": 0,
  "ca": 0,
  "thal": 1
}
```

Example Response:

```json
{
  "prediction": 1
}
```

---

# Learnings

- Production deployment of ML models
- FastAPI model serving
- Docker containerization
- Kubernetes orchestration
- Horizontal Pod Autoscaling
- GitHub Actions CI/CD
- SHAP Explainability
- Fairness Testing with Fairlearn
- Cloud Logging Observability
- Drift Detection
- Load Testing using wrk

---

# Author

**Abhishek Dutta**  
**Roll Number: 22F3001838**  
**IIT Madras BS Degree Program**
