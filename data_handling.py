import pandas as pd
from datetime import datetime as dt
from time import gmtime, strftime
import os

def limpar_arquivo(odate): 
    # leitura do csv como dataframe
    csv_path = '/app/raw/NFS/NFS-GROUP-%s.csv' %(odate)
  
    df = pd.read_csv(csv_path)

    # limpa os valores nulos do dataframe
    df_nan = df.dropna()

    # garante que a Data_Solicitacao seja um datetime
    df_nan['data_vencimento'] = pd.to_datetime(df_nan['data_vencimento'], format='%d/%m/%Y')

    csv_new_file = 'NFS-GROUP-TRUSTED-%s.csv' %(odate)

    # upload na pasta de trusted
    csv_new_path = '/app/trusted/NFS/'+ csv_new_file

    print(f".csv criado em '{csv_new_path}'\n")
