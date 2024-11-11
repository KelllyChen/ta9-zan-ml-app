# ta9-zan-ml-app

Link to the deployed model: [http://35.229.43.40/](http://35.229.43.40/)

To run the code with your own deployed model, you will need to create an account with Google Cloud.

## File Breakdown

- **static/**: Folder containing `styles.css` for augmenting the frontend.
- **templates/**: Folder containing `index.html` to create the frontend.
- **model.py**: Machine learning model trained on a dataset, outputs a `.pkl` model file.
- **app.py**: Flask app creation script.
- **requirements.txt**: List of dependencies required to run the Python files.
- **Dockerfile**: Script to create the Docker image.
- **deployment.yaml**: Kubernetes deployment file for GKE.
- **service.yaml**: Kubernetes service file for GKE.

## Google Cloud Setup

Add the following files to the editor in the Google Cloud Console:

- **Project ID**: `clouddemo-440721`
- **Image Name**: `ml-app`
- **Tag**: `v7`

Make sure to adjust these values if you plan to run this on your own GKE account.

## Steps to Deploy on GKE

1. **Build the Docker image**:
   ```bash
   docker build -t gcr.io/clouddemo-440721/ml-app:v7 .
2. **Push the Docker image to Google Container Registry**:

   ```bash
   docker push gcr.io/clouddemo-440721/ml-app:v7

3. **Create the GKE cluster**:

   ```bash
   gcloud container clusters create demo-cluster \
    --num-nodes 1 \
    --region us-east1 \
    --machine-type e2-small \
    --disk-type pd-standard

4. **Get the credentials for the GKE cluster**:

   ```bash
   gcloud container clusters get-credentials demo-cluster --region us-east1

5. **Deploy the application on Kubernetes**:

   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml

6. **Get the service address to access your deployed model**:

   ```bash
   kubectl get services
