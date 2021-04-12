# For more information, please refer to https://aka.ms/vscode-docker-python
FROM postgres:latest
FROM python:latest

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./cdd /cdd
WORKDIR /cdd

EXPOSE 5432
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:api"]