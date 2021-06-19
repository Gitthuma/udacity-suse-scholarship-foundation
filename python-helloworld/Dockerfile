#Specify base image to use to run our application
FROM python:3.8

#Add metadata to our image
LABEL maintainer="Katie Gamanji"

#Copy files from local host to the container
COPY . /app

#Set the working directory
WORKDIR /app

#Install dependancies that the app will need
RUN pip install -r requirements.txt

#Specify how to start our application
CMD [ "python", "app.py" ]