# Healthcare claims classifier

Python application to demonstrate the health fact classifier

Follow the steps below to run the application:

1. Build the docker image:

`docker build -t healthpred .`

3. Run the image:

`docker run -it -p 80:80 healthpred`

4. The app accepts **GET** requests on port 80. Run the following sample command to test the app:

`curl http://localhost/PredictClass/"The news of the bomb blast in townsville is fake"/"There has been a bomb blast in the city of townsville"`

If the app is running correctly, you should get the following response in content:

`{"Predicted Class":"False"}` 