# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install system dependencies and Python dependencies
RUN apt-get update && \ 
    apt-get install -y --no-install-recommends build-essential libgomp1 && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files into container
# Copy only necessary files
COPY requirements.txt . 
COPY app.py . 
COPY models/ ./models
COPY templates/ ./templates

# Expose Flask port
EXPOSE 5000

# Use Gunicorn to run the app
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]
