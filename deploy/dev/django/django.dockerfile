FROM python:3.12.3

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working Directory
WORKDIR /misc/project/job-noti

# Install Requirements
COPY poetry.lock .
COPY pyproject.toml .

RUN pwd
RUN pip install --upgrade pip && pip install poetry

# Copy the rest of the project
COPY . .
RUN poetry install

# run entrypoint.sh
RUN chmod +x deploy/dev/django/run.sh

ENTRYPOINT [ "deploy/dev/django/run.sh" ]
