# Base image with Python
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the calculator script into the container
COPY calculator.py .

# Define the command to run the calculator
CMD ["python", "calculator.py"]
