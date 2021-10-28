## Healthcare claims classifier

We fine tuned the `Longformer-base-4096` model from Huggingface for a classification task on Health fact dataset. 

Input : Main_text, Claim

Output: Label (true, false, unproven, mixture) 

The model has been fine tuned on google colab with a single gpu. To avoid the cuda memory issues the batch size used is 1. Also, to avoid running into colab timeout issues I have trained 1-3 epochs at one go to have a total of 12 epochs of training.
The notebook describes the training code.

*Note: The training code expects train, dev, test folders inside PUBHEALTH folder having respective data.tsv files inside them* 

## Results:
Train accuracy: 91.4%
Validation accuracy: 78.0%
Test Accuracy: 76.4 %, Average F1 score: 0.77

The trained model can be accessed using the Python application:

Follow the steps below to run the application:

1. Download the trained model from [google drive link] (https://drive.google.com/drive/folders/1t2p4h1cSbvpf7kAwKTUlXmAc8dnZxCAa?usp=sharing) and keep it in the root directory.

2)Build the docker image:

`docker build -t healthpred .`

3. Run the image:

`docker run -it -p 80:80 healthpred`

4. The app accepts **GET** requests on port 80. 

Run the following command format to query the model:

`curl http:localhost/PredictClass/<main_text>/<claim>`

`curl http://localhost/PredictClass/"The news of the bomb blast in townsville is fake"/"There has been a bomb blast in the city of townsville"`

If the app is running correctly, you should get the following response in content:

`{"Predicted Class":"False"}` 

***Suggestions to improve the model***:

1) Extract only the relevant sentences from main_text as evidence (the sentences which closely match with the claim text) along with claim text.
2) Or Try extractive or abstractive summaries for main_text field and use that as input along with the claim text.
3) Train the model for more epochs. Increase the batch size to 16 or 32 is sufficient gpu memory is available.
4) Try using T5, or pegasus model ( which is trained to extract important sentences for a text) with a suitable classification head as the base models for fine tuning.
