# Use a Python 3.9 image as the base
FROM ubuntu:latest

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      openssh-server \
      iputils-ping

# Copy the Python script into the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

RUN useradd -rm -d /home/admin -s /bin/bash -p admin admin

EXPOSE 22

# Run the Python script continuously
ENTRYPOINT [ "/app/entrypoint.sh" ]