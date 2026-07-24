# Use the official lightweight Python image as the base environment
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all project files from the local machine into the container
COPY . .

# Install all project dependencies
RUN pip install -r requirements.txt

# Document that the application listens on port 8000
EXPOSE 8000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]