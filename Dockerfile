# Use a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]

