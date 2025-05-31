
# Stage 1: Build dependencies and compile


FROM python:3.13 AS builder

WORKDIR /app

# copying the requirements
COPY requirements.txt .

#  installing the requirements - Python dependencies
RUN pip install --upgrade pip
RUN pip install --user --no-cache-dir --upgrade -r requirements.txt


# Stage 2: slim runtime image

FROM python:3.13-slim AS production 

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

CMD [ "python", "backend/app/main.py" ]



