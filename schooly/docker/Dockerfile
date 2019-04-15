# Based off of image with python and other useful stuff installed
FROM python:3
ENV PYTHONUNBUFFERED 1

# Install any dependencies and requirements
COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/base.txt

# Prep the entrypoint script
COPY ./docker/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh

# Copy in the source code, set working directory to the source code folder
COPY ./web /code
WORKDIR /code