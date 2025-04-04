# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt update && apt install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script and input file
COPY script.py .
COPY input.txt .

# Run the script
CMD ["python", "script.py"]
