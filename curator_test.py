import os
import boto3
import curator
import logging

from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection


# Adding a logger isn't strictly required, but helps with understanding Curator's requests and debugging.
logger = logging.getLogger('curator')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

host = os.environ['AWS_ES_HOST_URL']
region = os.environ['AWS_REGION']
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
