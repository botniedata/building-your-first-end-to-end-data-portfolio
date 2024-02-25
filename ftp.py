# import packages
import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

# ftp login credentials
def get_ftp() -> FTP_TLS:

    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]

    # return authentication of FTP
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()
    return ftp

# upload to ftp
def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        # specify the destination directory in the STOR command
        destination_directory = "/home/ftpuser/ftp"
        destination_path = f"{destination_directory}/{file_source.name}"
        ftp.storbinary(f"STOR {destination_path}", fp)
        

def delete_file(file_source: str | Path):
    remove(file_source)
    

def pipeline():
    
    # load source configuration
    with open("config.json", "rb") as fp:
        config = json.load(fp)

    ftp = get_ftp()  

    # loop each config (source_name and params)
    for source_name, source_config in config.items():
        file_name = Path(source_name + ".CSV")
        df = read_csv(source_config)
        df.to_csv(file_name, index=False)
        print(f"Downloading {file_name} File Successfully Done!")

        upload_to_ftp(ftp, file_name)
        print(f"Uploading {file_name} File to FTP Server Successfully Done!")

        delete_file(file_name)
        print(f"Deleting {file_name} File Successfully Done!")
     
def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

if __name__=="__main__":

    # schedule pipeline
    schedule.every().day.at("16:56").do(pipeline)

    while True:
        schedule.run_pending()
        time.sleep(1)