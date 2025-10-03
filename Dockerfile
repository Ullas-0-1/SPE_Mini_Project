#base python image
FROM python:3.9-slim

# new working directory
WORKDIR /code

#Copying only the requirements file and installing dependencies first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY ./app /code/app

# Exposing the port the app runs on
EXPOSE 80

# command to run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]