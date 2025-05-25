FROM python:3.10-slim

WORKDIR /app

# System dependencies (in case you scrape or use NLP)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your local codebase into the container
COPY . .

# Copy .env if needed (safe for local dev, not for Git)
# COPY .env .   <-- Only if you’re NOT using Render env var panel

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
