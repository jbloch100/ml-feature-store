# ML Feature Store

## Overview
Lightweight in-memory feature store for machine learning applications. Supports entity-feature ingestion, retrieval, and summary reporting.

## Features
- Ingests features per entity ID
- Retrieves features on demand
- Computes feature count summaries
- CLI output of feature data

## Run
```bash
python src/main.py
```

## Test
```bash
python -m unittest tests/test_main.py
```

---

## Docker

### Build
```bash
docker build -t ml-feature-store .
```

### Run
```bash
docker run --rm ml-feature-store
```

### Test
```bash
docker run --rm ml-feature-store python -m unittest discover -s tests
```