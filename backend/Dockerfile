FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run the application
CMD ["python", "main.py"]
