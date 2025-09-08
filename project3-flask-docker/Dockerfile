# Python image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run Flask app
CMD ["python", "app.py"]
