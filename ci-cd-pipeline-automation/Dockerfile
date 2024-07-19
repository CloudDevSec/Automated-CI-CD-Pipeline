# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Command to run the application
CMD ["python", "app/main.py"]
