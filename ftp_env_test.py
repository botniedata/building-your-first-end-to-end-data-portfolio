import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

# ftp credentials
def get_ftp() -> FTP_TLS:
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]
    FTPPORT = environ["FTPPORT"]

    # display ftp credentials from virtual environment
    print(f"the host is: {FTPHOST}")
    print(f"the host is: {FTPUSER}")
    print(f"the host is: {FTPPASS}")
    print(f"the host is: {FTPPORT}")

    # return authentication of FTP
    # ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    # ftp.prot_p()
    # return ftp

if __name__=="__main__":
    
    get_ftp()