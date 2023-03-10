# Comic-Layaway
This is a Flask-based backend for Layaway Comics. It is contained within a Docker container for ease of deployment.

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Before you begin, you will need to have the following software installed on your machine:

- Docker
- Python 3
- pip

## Installing
1. Clone this repository:
```bash
git clone https://github.com/guillermoreyesv/Comic-Layaway.git
```

2. Navigate to the repository directory:
```bash
cd Comic-Layaway
```

3. Copy the .env.example file to .env:
```bash
cp .env.example .env
```
4. Open the .env file and update the values to match your environment.

### Using docker
5. Make docker network
```bash
docker network create --subnet=172.18.0.0/16 marvel-network
```

6. Build the Docker container:
```bash
docker build -t comics-layaway .
```

7. Run the container:
```bash
docker run -d -p 8002:8002 --network marvel-network --ip 172.18.0.12 --name layaway-container comics-layaway
```

8. Your Comic-Layaway should now be up and running in http://127.0.0.1:8002!

### In local

5. Start a virtualenv:
```python
py -m venv .python-version
```

6. Activate virtualenv:
```bash
.\.python-version\Scripts\Activate.ps1
```

7. Install the required packages:
```python
pip install --no-cache-dir -r requirements.txt
```

8. Start the application:
```bash
python run.py
```

9. Your Comic-Layaway should now be up and running in http://127.0.0.1:5000!

## Deployment
To deploy this application to a production environment, you will need to follow the steps above, making any necessary modifications to match your environment.

## Built With
- <ins>Flask</ins> - A lightweight Python web framework.
- <ins>MongoDB</ins> - A NoSQL document-oriented database.
- <ins>Docker</ins> - A platform for building and deploying applications in containers.