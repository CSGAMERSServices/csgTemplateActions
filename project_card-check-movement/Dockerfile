FROM python:3

# Copy requirements.txt and install the action dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY script.py /script.py

# Run our script.py as our docker entrypoint by python
CMD ["python", "/script.py"]