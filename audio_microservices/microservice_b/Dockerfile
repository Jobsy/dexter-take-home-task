# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY microservice_b .

# CMD ["python", "app.py"]


# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# CMD ["python", "app.py"]

FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]

