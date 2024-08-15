# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
