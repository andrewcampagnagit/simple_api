FROM python:3.7.3
WORKDIR /project
ADD . /project
RUN pip install Flask
CMD ["python","app.py"]