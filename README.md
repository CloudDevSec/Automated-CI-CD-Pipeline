# Automated CI/CD Pipeline

This project sets up a complete CI/CD pipeline for a sample application using Jenkins, GitHub Actions, Docker, and Kubernetes.

## Technologies

- Jenkins
- GitHub Actions
- Docker
- Kubernetes

## Installation and Usage

### Jenkins

1. Install Jenkins and set up a new job.
2. Use the `Jenkinsfile` in this repository for pipeline configuration.

### GitHub Actions

1. GitHub Actions is already set up with the configuration in `.github/workflows/ci-cd.yml`.
2. Push your code to the GitHub repository to trigger the actions.

### Docker

1. Build the Docker image:
    ```bash
    docker build -t sample-app .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 sample-app
    ```

### Kubernetes

1. Apply the Kubernetes manifest files:
    ```bash
    kubectl apply -f kubernetes/
    ```

## Contact

Sascha Meyer
