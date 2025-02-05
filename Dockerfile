# Use the Python 3.9 slim image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app


# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install  --upgrade pip \
    && pip install  -r requirements.txt

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
CMD ["python", "App/app.py"]
