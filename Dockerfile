FROM python:3.10-slim


WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt


EXPOSE 5000


ENV NAME World


CMD ["python", "app.py"]
#END OF FILE
