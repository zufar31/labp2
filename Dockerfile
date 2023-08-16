# Use the arm32v7/python:3 base image
FROM arm32v7/python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Main1.py and hal folder into the container
COPY Main1.py ./
COPY hal ./hal

# Install required Python libraries: telepot, pyserial, and rpi.gpio
RUN pip install --no-cache-dir telepot pyserial rpi.gpio

# Trigger the Python script (Main1.py) when the container starts
CMD ["python", "./Main1.py"]

