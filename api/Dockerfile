# Use a Python 3.9 image as the base
FROM python:3.9

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      sshpass \
      iputils-ping

# Copy api folder into the container directory
COPY . /api

# Set the working directory to /api
WORKDIR /api

# Use a Python 3.9 image as the base
RUN pip install -r requirements.txt