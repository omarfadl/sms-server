FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies (optional but often useful)
RUN apt-get update && apt-get install -y build-essential

# Copy your code and requirements
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Default command to run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]