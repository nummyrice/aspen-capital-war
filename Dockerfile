# FROM node:16 AS build-stage

# WORKDIR /react-app
# COPY react-app/. .



FROM python:3.9.4

# Setup Flask environment
ENV FLASK_APP=api
ENV FLASK_ENV=development
ENV SQLALCHEMY_ECHO=True

EXPOSE 5001

WORKDIR /api
COPY . .
# COPY --from=build-stage /react-app/build/* app/static/

# Install Python Dependencies
RUN pip install -r requirements.txt
RUN pip install psycopg2

# Run flask environment
CMD flask run
