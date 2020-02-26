FROM python:3.8.0-alpine

# Install dependencies
RUN pip install flask flask-bootstrap4

# Copy our code into the container
COPY app.py .
# Some metadata

EXPOSE 5000
# Set the FLASK_APP environment variable

ENV FLASK_APP app.py
CMD [ "flask", "run", "--host=0.0.0.0" ]
