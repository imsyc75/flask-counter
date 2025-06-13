# flask-counter
A simple Flask counter application deployed with CI/CD pipeline.

## Deployment
This application is automatically deployed to Render.com when changes are pushed to the main branch.
Live Application: https://flask-counter-umb8.onrender.com

## Local Development

Clone the repository
Install dependencies: pip install -r requirements.txt
Run the application: flask run

## Docker
The application can be built and run using Docker:
bashdocker build -t flask-counter .
docker run -p 8080:8080 flask-counter

## CI/CD Pipeline
The deployment pipeline is configured using GitHub Actions and automatically:

Checks out the code
Sets up Python environment
Installs dependencies
Runs tests (if available)
Deploys to Render.com

The pipeline is triggered on every push to the main branch.