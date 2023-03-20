FROM python:3.10.10-slim
WORKDIR /home/
COPY requirements.txt requirements.txt
COPY src/ src/
RUN pip install -r  requirements.txt
EXPOSE 8000
CMD [ "python", "src/main.py"]