# Use the Python 3.12 slim image as a base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app


# Install Python dependencies
# COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install  -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD python ./App/app.py
