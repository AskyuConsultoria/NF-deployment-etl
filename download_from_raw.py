import boto3
import os
from datetime import datetime 

def baixar_arquivo_raw(bucket_name, odate):

    s3_file_path = f'NFS-GROUP-{odate}.csv'
    local_file_path = f'/app/raw/NFS/NFS-GROUP-{odate}.csv' 
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_file_path, local_file_path)

    print(f"Arquivo CSV baixado para: {local_file_path}")