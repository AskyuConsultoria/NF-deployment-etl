import time
from time import gmtime, strftime
import os
import boto3
import logging
from botocore.exceptions import ClientError



def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')  
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def realizar_upload(bucket_trusted, odate):
    csv_path = f'/app/trusted/NFS/NFS-GROUP-TRUSTED-{odate}.csv' 
    bucket_name = bucket_trusted
    print('Carregando no bucket\n')

    upload_file(csv_path, bucket_name, csv_path)
    print(f"arquivo '{csv_path}' carregado em '{bucket_name}' ")
