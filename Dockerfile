# Use a lightweight Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /home/data

# Copy the necessary files into the container
COPY scripts.py /home/data/scripts.py
COPY IF.txt /home/data/IF.txt
COPY AlwaysRememberUsThisWay.txt /home/data/AlwaysRememberUsThisWay.txt

# Create the output directory
RUN mkdir -p /home/data/output

# Install necessary Python libraries (if any)
RUN pip install --no-cache-dir --upgrade pip

# Set the default command to run the Python script
CMD ["python", "/home/data/scripts.py"]
