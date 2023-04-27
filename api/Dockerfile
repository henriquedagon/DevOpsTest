# Use a Python 3.9 image as the base
FROM python:3.9

# Set the working directory to /api
WORKDIR /api

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
      sshpass \
      iputils-ping

# Use a Python 3.9 image as the base
# Put python pip install before COPY other files to use cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy api folder into the container directory
COPY . .

CMD ["python", "-u", "api.py"]