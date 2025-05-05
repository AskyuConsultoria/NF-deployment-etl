import pandas as pd
from datetime import datetime as dt
from time import gmtime, strftime
import os

def limpar_arquivo(odate): 
    # leitura do csv como dataframe
    csv_path = '/app/raw/NFS/NFS-GROUP-%s.csv' %(odate)

    df = pd.read_csv(csv_path, sep=";")

    # limpa os valores nulos do dataframe
    df_nan = df.dropna()

    print("Colunas disponíveis:", df_nan.columns.tolist())
    print(df_nan.head())


    # garante que a Data_Solicitacao seja um datetime
    df_nan['data_vencimento'] = pd.to_datetime(df_nan['data_vencimento'], format='%d/%m/%Y')

    csv_new_file = 'NFS-GROUP-TRUSTED-%s.csv' %(odate)

    # upload na pasta de trusted
    csv_new_path = '/app/trusted/NFS/'+ csv_new_file
    os.makedirs(os.path.dirname(csv_new_path), exist_ok=True)

    df_nan.to_csv(csv_new_path, index=False, enconding="utf-8-sig")
    print(f".csv criado em '{csv_new_path}'\n")
