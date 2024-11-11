# ta9-zan-ml-app

Link to the deployed model: http://35.229.43.40/

to run the code for your own deployed model you will need to make an account with google cloud

File breakdown
static: folder containing styles.css for augmenting frontend app
templates: folder containing index.html which creates frontend
model.py: ml model trained on a dataset, outputs a model in .pkl format
app.py: file to create a flask app
requirements.txt: requirements to run the python files
dockerfile: file to create docker image
deployment.yaml: deployment file for gke
service.yaml: service file for gke

Add these files to the editor in the google cloud console
project id: clouddemo-440721
image name: ml-app
tag: v7
Adjust the above accordingly if you plan to run this on your own gke account
Run the following commands in the gke terminal, get services will give the address to access your deployed model
docker build -t gcr.io/clouddemo-440721/ml-app:v7 .
docker push gcr.io/clouddemo-440721/ml-app:v7
gcloud container clusters create demo-cluster --num-nodes 1 --region us-east1 --machine-type e2-small --disk-type pd-standard​​
gcloud container clusters get-credentials demo-cluster --region us-east1
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get services
