# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
