FROM python:3.12.3

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working Directory
WORKDIR /misc/project/aiapi_prod

# Install Requirements
COPY requirements  requirements
RUN pip install --upgrade pip && pip install -r requirements/prod.txt

# Install xvfb for virtual display
RUN apt-get update -y && apt-get install -y xvfb

# Copy the rest of the project
COPY . .

# run entrypoint.sh
RUN chmod +x deploy/prod/django/run.sh

ENTRYPOINT [ "deploy/prod/django/run.sh" ]
