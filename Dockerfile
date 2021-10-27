FROM python:3.7
RUN apt-get update 
RUN apt-get -y install python3-pip
COPY ./app /app
COPY /requirements.txt /
COPY ./health_fact_classifier /health_fact_classifier
# Create volume mount point for GPT2 language model files
VOLUME /data

#Install dependencies
RUN pip install -r /requirements.txt

#Expose port outside container
EXPOSE 80

#Run the perplexity score app
ENTRYPOINT ["uvicorn", "app.predict:app", "--host", "0.0.0.0", "--port", "80"]
