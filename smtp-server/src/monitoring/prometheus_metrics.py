
from prometheus_client import Counter, Gauge
from fastapi import FastAPI

# Define metrics
emails_processed = Counter('emails_processed_total', 'Total emails processed')
active_connections = Gauge('smtp_active_connections', 'Current active SMTP connections')

def setup_metrics(app: FastAPI):
    # Add Prometheus metrics endpoint
    from prometheus_client import make_asgi_app
    metrics_app = make_asgi_app()
    app.mount("/metrics", metrics_app)
