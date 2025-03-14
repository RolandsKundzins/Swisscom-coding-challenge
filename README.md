# Swisscom coding challenge

## To start the project

`docker compose up --build`

## TO run the automated tests:

- For flask-backend:
  `docker compose run --rm flask-app pytest`
- For vue-frontend:
  `docker compose exec playwright-tests npx playwright test`

# Additional information

## Datahub client usage examples

- https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/dataset_query_entity_v2.py
- https://github.com/datahub-project/datahub/blob/master/metadata-ingestion/examples/library/dataset_query_description.py

## Dataset docs:

- https://datahubproject.io/docs/graphql/objects#dataset

## Graphql usage example

- https://datahubproject.io/docs/api/graphql/getting-started/
