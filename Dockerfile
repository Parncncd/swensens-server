FROM python:3.11.9-bullseye
WORKDIR /usr/src/app
COPY  . /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./main.py
