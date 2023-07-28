# docker_implementation
practical implementation of how to containerize ML models

1. create an ML model (eg. diabetes prediction)
2. create a pkl file of the model
3. deploy the model using Flask and Flasgger
4. run docker
5. build a docker image of the ML model (docker build -t <name of img> . )
6. containerize the image  (docker run -p 8081:8081 <name of img> )
