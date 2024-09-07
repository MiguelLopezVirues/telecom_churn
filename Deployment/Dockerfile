# Start from Python image
FROM python:3.11.9-slim

ENV PYTHONUNBUFFERED=1

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

# Copy your environment.yml file

RUN pipenv install --system --deploy 

COPY . /app

# Activate the environment and set it as default for RUN instructions
# SHELL ["conda", "run", "-n", "churn_deployment", "/bin/bash", "-c"] 

EXPOSE 9696
ENTRYPOINT ["gunicorn","--bind=0.0.0.0:9696","predict_request:app"]