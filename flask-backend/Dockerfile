# Regularly updated to the latest version of Python
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
# --no-cache-dir for reducing the image size
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of code
COPY . .

EXPOSE 5000

CMD ["gunicorn", "--reload", "--workers=2", "--timeout=120", "--bind=0.0.0.0:5000", "api:app"]
