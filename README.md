# ML Feature Store

## Overview
A minimal in-memory feature store to ingest and retrieve entity features for ML model serving.

## Features
- Ingest feature dictionaries per entity (e.g. user, ad)
- Retrieve features for model inference
- Summarizes entity-to-feature mappings

## Run
```bash
python src/main.py
```

## Test
```bash
python -m unittest tests/test_main.py
```
