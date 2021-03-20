FROM python:3.9
RUN pip3 install flask
COPY server.py .
CMD ["python3", "server.py"]
