# 1. Start from a base image
FROM python:3.9-slim

# 2. Set a general working directory inside the container
WORKDIR /code

# 3. Copy only the requirements file and install dependencies first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your entire local 'app' directory into a new 'app' directory inside /code
# This creates the /code/app structure that your Python imports expect.
COPY ./app /code/app

# 5. Expose the port the app runs on
EXPOSE 80

# 6. Define the command to run your application
# This tells uvicorn to look inside the 'app' folder for 'main.py' and find the 'app' object
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]