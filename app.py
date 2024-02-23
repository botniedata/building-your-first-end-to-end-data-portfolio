from ftplib import FTP_TLS

# FTP details
ftphost = "localhost" # replace with your FTP ip address or just localhost
ftpuser = "ftpuser" # replace with your FTP username
ftppass = "ftp123456" # replace with your FTP password
ftpport = 21

# Login to FTP
ftp = FTP_TLS()
ftp.connect(ftphost, ftpport)
ftp.login(ftpuser, ftppass)
ftp.prot_p() # Fix on 522 Data connections must be encrypted.

# Create sample file
with open("test.txt", "w") as fp:
    fp.write("This is my sample message\n")
    fp.write("Another sample message\n")
    fp.write("bye\n")

# Upload file to FTP 
with open("test.txt", "rb") as fp:
    ftp.storbinary("STOR test_ftp.txt", fp)

# Download file from FTP 
with open("test_download.txt", "wb") as fp:
    ftp.retrbinary("RETR test_ftp.txt",fp.write)

# Delete file from FTP
ftp.delete("test_ftp.txt")

# If this line gets printed, you have successfully 
# established connection to the WSL FTP Server. 
print("Upload, download, delete tests complete")