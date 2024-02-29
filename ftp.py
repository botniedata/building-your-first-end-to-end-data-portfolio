# import packages
from ftplib import FTP_TLS          # interacting with FTP Server with TLS
from ftplib import FTP              # interacting with FTP Server
import sys                                    
import json                         # used for reading and writing JSON data
import time                         # used for scheduling tasks
import schedule                     # used for scheduling tasks
import pandas as pd                 # used for working with CSV data
from os import environ, remove      # used for interacting with operating system and deleting files
from pathlib import Path            # used for working with file path

# ftp login credentials
def get_ftp() -> FTP_TLS:           # retrieves the FTP credentials from environment variables and establishes a secure connection to the FTP server.

    FTPHOST = environ["FTPHOST"]    # FTP server hostname or IP address
    FTPUSER = environ["FTPUSER"]    # Username for the FTP server
    FTPPASS = environ["FTPPASS"]    # Password for the FTP server

    # return authentication of FTP
    # ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)        # creates an instance of the FTP_TLS class from the ftplib module
    ftp.prot_p()                                    # method enables protection for the data connection used for file transfer
    return ftp                                      # returns the object ftp, which represents the established secure connection to the FTP server

# upload to ftp
def upload_to_ftp(ftp: FTP_TLS, file_source: Path):                         # uploads a file to the specified directory on the FTP server
    with open(file_source, "rb") as fp:                                     # with statement to open the local file specifed by file_source in read-binary mode ('rb')
        # specify the destination directory in the STOR command             # assigned the open file object to the variable fp
        destination_directory = "/home/ftpuser/ftp"                         # specified the destination directory on the FTP server where the file will be uploaded
        destination_path = f"{destination_directory}/{file_source.name}"    # full destination path on the FTP server by combining the specified destination directory and file name from the local file
        ftp.storbinary(f"STOR {destination_path}", fp)                      # actual file upload method from ftplib library used for efficient binary file tranfers
    
def delete_file(file_source: str | Path):                                   # deletes a file from the local system
    remove(file_source)
    
# pipeline
def pipeline():                                                             
    
    # load source configuration
    with open("config.json", "rb") as fp:                                   # loads the configuration from a JSON file named "config.json"
        config = json.load(fp)

    ftp = get_ftp()                                                         # establishes an FTP connection using get_ftp()

    # loop each config (source_name and params)
    for source_name, source_config in config.items():                       # creates a for loop to iterate the key value pairs of the config dictionary
        file_name = Path(source_name + ".CSV")                              # creates a new Path object named file_name using the source_name from the dictionary
        df = read_csv(source_config)                                        # reads the CSV data from the specified URL using read_csv()
        df.to_csv(file_name, index=False)                                   # saves the data as a CSV file with the source name, excluding row index being included in the save CSV file
        print(f"Downloading {file_name} File Successfully Done!")

        upload_to_ftp(ftp, file_name)                                               # uploads the CSV file to the FTP server using upload_to_ftp()
        print(f"Uploading {file_name} File to FTP Server Successfully Done!")                       

        delete_file(file_name)                                                      # deletes the loacl CSV file using delete_file()  
        print(f"Deleting {file_name} File Successfully Done!")
     
def read_csv(config: dict) -> pd.DataFrame:                 # this function retrieves data from a CSV file located at a specified URL and returns the data as a pandas DtaFrame
    url = config["URL"]                                     # dictionary containing configuration information for the CSV download. URL of the CSV file to be downloaded
    params = config["PARAMS"]                               # (optional) dictionary containing additional parameters to be passed to the pandas.read_csv() function
                                                            # can further customize the CSV reading process, such as specifying delimiters encoding, or skipping rows
    return pd.read_csv(url, **params)                       # unpacked using the double star (**) to pass them as keyword arguements.

if __name__=="__main__":                                    # distinguish between direct execution and module usage. promotes modularity, testability and avoid potential issues when working with modules

    pipeline()                                              # calls function to execute the download, upload and deletion process.

    # # schedule pipeline
    # schedule.every().day.at("17:21").do(pipeline)         # how to schedule the pipeline() function to run daily on the specific military time using schedule library
                                                            # .every().day schduels the function to run every day and .at("hh:mm") execute time
    # while True:
    #     schedule.run_pending()                            # continiously checks for pending scheduled tasks
    #     time.sleep(1)                                     # creates a short delay of 1 second before checking again, preventing excessive CPU usage