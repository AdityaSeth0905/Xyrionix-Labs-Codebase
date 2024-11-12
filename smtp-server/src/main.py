
import uvicorn
from fastapi import FastAPI
from src.smtp.smtp_server import SMTPServer
from src.api.api_endpoints import api_router
from src.monitoring.prometheus_metrics import setup_metrics

app = FastAPI(title="Advanced SMTP Server")

# Add API routes
app.include_router(api_router)

# Setup Prometheus metrics
setup_metrics(app)

# Initialize SMTP Server
smtp_server = SMTPServer()

if __name__ == "__main__":
    smtp_server.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
