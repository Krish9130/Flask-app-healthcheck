# Step 1: Use an official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory (your app) into the container's working directory
COPY . /app

# Step 4: Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 5000 for Flask app
EXPOSE 5000

# Step 6: Set the environment variable for Flask app to not run in debug mode
ENV FLASK_ENV=production

# Step 7: Use Gunicorn to serve the Flask application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
