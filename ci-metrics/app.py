from fastapi import FastAPI
from prometheus_client import Gauge, generate_latest
from starlette.responses import Response

app = FastAPI()

build_duration = Gauge('ci_build_duration_seconds', 'Duration of build')
build_status = Gauge('ci_build_status', 'Build success=1, fail=0')

@app.get("/metrics")
def metrics():
    build_duration.set(120.3)  # example value
    build_status.set(1)        # success
    return Response(generate_latest(), media_type="text/plain")
