FROM python:3.7.3
WORKDIR /project
ADD . /project
EXPOSE 8080
RUN pip install Flask
CMD ["python","app.py"]