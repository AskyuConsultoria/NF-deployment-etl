import boto3
import os
from datetime import datetime 

# Definir o nome do bucket e o caminho do arquivo


# Nome do Bucket RAW
def baixar_arquivo_raw(bucket_name, odate):

    s3_file_path = 'NFS-GROUP-%s.csv' %(odate)
    local_file_path = '''~/raw_files/NFS/NF-GROUP-%s.csv''' %(odate)
    local_file_path = os.path.expanduser(local_file_path)

    s3 = boto3.client('s3')
    s3.download_file(bucket_name, s3_file_path, local_file_path)

    print(f"Arquivo CSV baixado para: {local_file_path}")
