from transformers import LongformerTokenizer, LongformerForSequenceClassification, LongformerConfig
from fastapi import FastAPI
import numpy as np
import uvicorn
import torch

app = FastAPI()
model_name_or_path='health_fact_classifier'
model_config = LongformerConfig.from_pretrained(pretrained_model_name_or_path='allenai/longformer-base-4096', num_labels=4)
model_config.vocab_size=50266
# Load pre-trained model (weights)
with torch.no_grad():
        model = LongformerForSequenceClassification.from_pretrained(model_name_or_path,config=model_config)
        model.eval()
        
# Load pre-trained model tokenizer (vocabulary)
tokenizer = LongformerTokenizer.from_pretrained("allenai/longformer-base-4096")

def predict(maintext,claim):
    global tokenizer, model
    tokenize_input = tokenizer.encode(maintext,claim)
    tensor_input = torch.tensor([tokenize_input])
    logits = model(tensor_input)['logits']
    #logits = logits.numpy()
    # get predicitons to list
    predId = logits.argmax(axis=-1).flatten().tolist()
    id2labels ={0:"True",1:"False",2:"Unproven",3:"Mixture"}

    return id2labels[predId[0]]

@app.get("/")
def read_root():
    return {"Error": "Sentence is null"}


@app.get("/PredictClass/{maintext}/{claim}")
def PredictClass(maintext,claim):
    if maintext=="" or claim=="":
        return {"Error": "Claim or MainText cannot be null!"}
    else:
        return {"Predicted Class": str(predict(maintext,claim))}
