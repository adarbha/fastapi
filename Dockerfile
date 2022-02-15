FROM mcr.microsoft.com/mssql/server
FROM python:3.9

## SET WORKING DIRECTORY
WORKDIR /app

RUN apt-get update -y \
    && apt-get install -y wget \
    && apt-get install -y  --no-install-recommends unixodbc-dev \
    unixodbc \
    libpq-dev \
    && apt-get clean

COPY requirements.txt .

## INSTALL PIP DEPENDENCIES
RUN pip install -r requirements.txt

## COPY REST OF THE FILES
COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]