# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the script into the container
COPY setup.py .

# Install the requests library
RUN pip install requests

# Run the script
CMD ["python", "setup.py"]