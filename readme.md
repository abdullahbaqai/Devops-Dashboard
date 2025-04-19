# 🚀 DevOps Dashboard

A custom DevOps Dashboard that provides **real-time visual insights** into key performance metrics of the CI/CD pipeline, application health, and system performance. Built using **Grafana**, **Prometheus**, and custom monitoring agents.

---

## 📊 Features

- ✅ **CI/CD Pipeline Metrics**
  - Build success/failure rates
  - Deployment frequency
  - Test pass rates

- 🏥 **Application Health Monitoring**
  - HTTP response codes
  - Error rates
  - API latency and uptime

- 🖥️ **System Performance**
  - CPU & Memory usage
  - Disk I/O
  - Network throughput

- 📈 **Real-Time Visualization**
  - Beautiful, dynamic dashboards using Grafana
  - Alerts and thresholds for critical metrics

---

## 📁 Project Structure

Devops-Dashboard/ │ 
├── docker-compose.yml # Orchestrates Prometheus, Grafana, and metric exporters │ 

├── ci-metrics/ │ 

├── Dockerfile # Custom image for CI metric scraper │
 └── app.py # Python app exposing CI/CD metrics via HTTP │
 └── prometheus/
 └── prometheus.yml # Prometheus configuration for scraping metrics