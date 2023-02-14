import os
import boto3
from botocore.exceptions import ClientError
import json
from db_plugins.db.mongo.connection import _MongoConfig


def get_secret(secret_name: str):

    secret_name = secret_name
    region_name = "us-east-1"

    client = boto3.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    return get_secret_value_response["SecretString"]


def get_mongodb_credentials():
    secret_name = os.environ["MONGODB_SECRET_NAME"]
    secret = get_secret(secret_name)
    secret = json.loads(secret)
    # check if config is valid
    # _MongoConfig will raise error if the config has missing parameters
    _MongoConfig(secret)
    return secret