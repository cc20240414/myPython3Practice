# Use an official Python image (https://hub.docker.com/_/python)
# Tag: slim     -> only contains the minimal Debian packages needed to run python
#      bullseye -> suite code names for releases of Debian. Bullseye is the development codename for Debian 11.
FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install any needed packages
RUN apt update && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container but within docker network
# EXPOSE 80

# Run jupyter notebook when the container launches
CMD ["tail", "-f", "/dev/null"]
