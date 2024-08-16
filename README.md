## I deployed the application to google cloud service using docker, you can access it from the link here  [this link](http:/http://35.184.71.101//)

# How To Execute

## Getting Started

The API is written in Python and uses the Flask framework.

You can run the API on Docker, for this you need to have Docker installed on your device, you can go to the Docker installation document from [this link](https://docs.docker.com/get-docker/).

## How to Run?
You can pull and run the Docker image of the API directly on your device.

```sh
docker run -d -p 3000:5000 berquee/bc4m-case-study:v1.0
```
After running this command, the Docker image of the API will be pulled and run on localhost:3000. You can send a request from a browser or a tool like Postman.
## What API Does?
#### GET Methods
1- Requests to the / path with the GET method in the API will send a fixed message:
{"msg":"BC4M"}
![localhost5000](https://github.com/user-attachments/assets/80852f9f-0693-4631-8180-62c6580d4f0e)

2- Requests to the /health path with the GET method return a fixed response, application health check can be performed:
{"status": "healthy"}
![localhosthealth](https://github.com/user-attachments/assets/227ae55c-34bf-428f-85d5-0c841f7ba296)

#### POST Methods
1- In requests sent to the / path with the POST method, the Json body sent to the API is sent back as a response.
###### Example:
![1](https://github.com/user-attachments/assets/90ea62dc-5414-4b1a-9512-49f9ebca74df)
![2](https://github.com/user-attachments/assets/a7195a3f-a73a-49e3-a36d-4ed08ef616da)
