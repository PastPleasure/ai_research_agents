# Bruk en base image med Python
FROM python:3.11-slim

# Sett arbeidsmappe
WORKDIR /app

# Kopier alt til /app
COPY . .

# Installer avhengigheter
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Eksponer porten som Streamlit bruker
EXPOSE 8501

# Kjør Streamlit appen
CMD ["streamlit", "run", "app.py"]
