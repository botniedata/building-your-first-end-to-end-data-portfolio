


---

### Create FTP User
- To create an FTP User <br>
    `sudo adduser ftpuser`

--- 

### Create `ftp` directory for FTP User 
- To create an `/ftp` directory use the command: <br>
    `sudo mkdir /home/ftpuser/ftp`

---        

### Provide Ownership of Directory
- This command provides ownership of the directory `/home/<user>/ftp` to the user and group `ftpuser` <br>
    `sudo chown ftpuser:ftpuser /home/ftpuser/ftp`

---

### Add the user `ftpuser` to the `nogroup`
- Using `usermod` to add the user `ftpuser` to the `nogroup` group. <br>
    `sudo usermod -aG nogroup ftpuser`

---

### Add `write` permission for the user `ftpuser` to `/home/ftpuser/ftp` directory
- Using `chmod` to tadd write permission for the owner of the directory `/home/ftpuser/ftp`. <br>

    `sudo chmod u+w /home/ftpuser/ftp`

### Install vsftpd
- Ensure that `vsftpd` (Very Secure FTP Daemon) is installed on your system. You can use your package manager to install: <br>
    `sudo apt-get install vsftpd`

---

### Back-up and Restore `vsftpd.conf` file
- To create an back-up file before creating any changes run this command: <br>
    `sudo cp /etc/vsftpd.conf /etc/vsftpd.conf_original `

- To restore back-up file to original configuration run this command: <br>
    `sudo cp /etc/vsftpd.conf_original /etc/vsftpd.conf `

--- 

### Configure vsftpd
- Open the `vsftpd.conf` file in a text editor (usually located in `/etc/vsftpd.conf`). <br>
    `sudo nano /etc/vsftpd.conf`
    - Ensure the following lines are set (uncomment): <br>
    ```ssl_enable=YES
    allow_anon_ssl=NO
    force_local_data_ssl=NO
    force_local_logins_ssl=NO
    ``` 
---

### Restart SSH
- restart the SSH Service <br>
    `sudo service ssh restart`
