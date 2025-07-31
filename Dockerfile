# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy source and test code
COPY src/ ./src/
COPY tests/ ./tests/

# Set environment variable for module imports
ENV PYTHONPATH=/app

# Default command to run main script
CMD ["python", "src/main.py"]