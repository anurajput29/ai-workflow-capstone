# AI in Production: Capstone Project

## Project Overview
This repository contains the end-to-end MLOps workflow, including data ingestion, automated unit testing, model evaluation, API deployment, and Docker containerization.

## Peer Review Checklist Mapping
- **Are there unit tests for the API/Model/Logging?** Yes, located in the `tests/` directory.
- **Can all unit tests be run with a single script?** Yes, run via `pytest`.
- **Is there a mechanism to monitor performance?** Yes, logging is tracked.
- **Is data ingestion automated?** Yes, implemented in `ingest.py`.
- **Were multiple models compared?** Yes, documented in our modeling notebooks.
- **Is everything containerized?** Yes, a working `Dockerfile` is included.
