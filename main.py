import data_handling
import download_from_raw
import upload_to_trusted
import argparse
import os 

def main():
    parser = argparse.ArgumentParser(description="Processa dados do bucket.")

    raw_unstructured_bucket = os.getenv("raw_unstructured_bucket")
    raw_structured_bucket = os.getenv("raw_structured_bucket")
    trusted_bucket = os.getenv("trusted_bucket")

    parser.add_argument("odate", help="Data de movimento da NF")
    parser.add_argument("--verbose", action="store_true", help="Modo verboso - Auxilia para debugar o código")

    args = parser.parse_args()

    if args.verbose:
        print("🟢 Executando em modo verboso")
        print(f"Data de movimento: {args.odate}")
        print(f"Bucket RAW não estruturado: {args.raw_unstructured_bucket}") 
        print(f"Bucket RAW estruturado: {args.raw_structured_bucket}")
        print(f"Bucket TRUSTED: {args.trusted_bucket}")

    download_from_raw.baixar_arquivo_raw(args.raw_structured_bucket, args.odate)
    data_handling.limpar_arquivo(args.odate)
    upload_to_trusted.realizar_upload(args.trusted_bucket, args.odate)


if __name__ == "__main__":
    main()





