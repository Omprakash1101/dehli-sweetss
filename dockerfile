# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port the app runs on (default for Django is 8000)
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the Django development server (or use another appropriate server for production, like Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi:app"]
