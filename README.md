# FastAPI CI/CD with ArgoCD

This is a simple FastAPI application demonstrating a complete CI/CD pipeline using GitHub Actions, Docker, ArgoCD and Kubernetes with Kind.

## Features

- FastAPI web application with health check endpoints
- Docker containerization
- Automated CI/CD pipeline with GitHub Actions
- Kubernetes deployment using Kind
- Image updates via ArgoCD (configured in the pipeline)

## Endpoints

- `GET /` - Home endpoint returning a success message
- `GET /health` - Health check endpoint

## Prerequisites

- Docker
- kubectl
- Kind (Kubernetes in Docker)

## Local Development

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CICD_ARGO_CD
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

4. Access the application at `http://localhost:8000`

## Deployment

### Using Kind

1. Create a Kind cluster:
   ```bash
   kind create cluster --name fastapi-cluster
   ```

2. Load the Docker image into Kind (optional, if not using registry):
   ```bash
   kind load docker-image <your-image> --name fastapi-cluster
   ```

3. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
   ```

4. Port forward the service:
   ```bash
   kubectl port-forward svc/fastapi-service 8000:80
   ```

5. Access the application at `http://localhost:8000`

### Via UI (NodePort)

If using Kind with a NodePort service, access via the node IP and port 30007.

## CI/CD Pipeline

The GitHub Actions workflow automates the following on push to main branch:

1. Builds the Docker image
2. Pushes to DockerHub
3. Updates the Kubernetes deployment.yaml with the new image tag
4. Commits and pushes the changes back to the repository

**Note:** The `k8s/deployment.yaml` file is ignored from triggering the pipeline to avoid infinite loops.

## Configuration

- Update DockerHub credentials in GitHub repository secrets: `DOCKER_USERNAME` and `DOCKER_PASSWORD`
- Modify Kubernetes manifests in the `k8s/` directory as needed