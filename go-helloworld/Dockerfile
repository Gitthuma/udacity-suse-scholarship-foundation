##Create the Docker image for the Go web application and push it to DockerHub, considering the following requirements:

#use the golang:alpine base image
FROM golang:alpine

#set the working directory to /go/src/app
WORKDIR /go/src/app

#copy all the files from the current directory to the container working directory
COPY . /go/src/app

#to build the application, use go build -o helloworld command, where -o helloworld will create the binary of the application with the name helloworld
#Added go mode init command
#Add && to run two commands
RUN go mod init && go build -o helloworld

#the application should be accessible on port 6111
EXPOSE 6112

#the command to start the container is to invoke the binary created earlier, which is ./helloworld
CMD [ "./helloworld" ]