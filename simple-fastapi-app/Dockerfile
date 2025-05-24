# using Python 3.11 slim image as base
FROM python:3.13-slim

# setting working directory inside the container
WORKDIR /app

# copying the requirements
COPY requirements.txt .

#  installing the requirements - Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#  copying appliction code to the working dir "/app" inside container
COPY . .

# exposing the port to 8000 on which the FastAPI web ap will run
EXPOSE 8000

# command to run the app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD [ "python", "main.py" ]

