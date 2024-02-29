
- [x] wsl installation
- [x] ubuntu update and upgrade
- [x] vsftpd installation
- [x] backup `etc/vsftpd.conf` file
- [x] configure `etc/vsftpd.conf` file
- [x] create `vsftpd.chroot_list`
- [x] restart vsftpd services
- [x] create non-sudo user
- [x] create non-sudo user ftp directory
- [x] change ownership for non-sudo user
- [x] remove root access for non-sudo user
- [x] add non-sudo user to `/etc/vsftpd.chroot_list` file
- [x] create a FTP test connection in a simple Python script
- [x] create python virtual environment
- [x] activate the virtual environment for `requirements.txt`
- [x] create file name as `requirements.txt`
- [x] adds ftp credentials to virtual environment
- [x] pip install `requirements.txt`
- [x] activate the virtual environment to run the `app.py`
- [x] unregister unix distro in WSL (Ubuntu)
- [x] reinstall again Ubuntu, install `vsftpd`, add `ftpuser`, configuration `/etc/vsftpd.conf`
- [x] remove `userprofile\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu*` from local machine
- [x] (optional) `userprofile\AppData\Local\Microsoft\Windows\WSL\`

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

### Add `write` permission for the user `ftpuser`
- Using `chmod` to tadd write permission for the owner of the directory `/home/ftpuser/ftp`. <br>

    `sudo chmod u+w /home/ftpuser/ftp`

### Install vsftpd
- Ensure that `vsftpd` (Very Secure FTP Daemon) is installed on your system. You can use your package manager to install: <br>
    `sudo apt-get install vsftpd`

--- 

### Configure vsftpd
- Open the `vsftpd.conf` file in a text editor (usually located in `/etc/vsftpd.conf`). <br>
    `sudo nano /etc/vsftpd.conf`
    - Ensure the following lines are set (uncomment): <br>
    ```ssl_enable=YES
    allow_anon_ssl=NO
    force_local_data_ssl=YES
    force_local_logins_ssl=YES
    ``` 
---

### Restart SSH
- restart the SSH Service <br>
    `sudo service ssh restart`

---

### This Configuration is Optional
### Generate SSL Certificate
- Generate a self-signed SSL certificate for FTP: <br>
    `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem`

---

### To use SSL Certificate and Key Generated
- To configure `vsftpd` configure `vsftptd.conf` file to use the SSL Certifcate and Key generated to `/etc/vsftpd.conf`. <br>
    `sudo nano /etc/vsftpd.conf`
    - add the following configuration:
    ```
    rsa_cert_file=/etc/ssl/private/vsftpd.pem
    rsa_private_key_file=/etc/ssl/private/vsftpd.pem
    ```
---

### Check OpenSSL Version
- Open terminal and run the command: <br>
    `openssl version`

---    

### Check OpenSSL Package Installation:
- On Linux system you can use a package manager to check if OpenSSL is installed: <br>
    `dpkg -l | grep openssl`

---    

### Check OpenSSL Executable
- Check OpenSSL executable is present on your system. Typical location is `/usr/bin/openssl`: <br>
    `ls /usr/bin/openssl`

---


### Restart vsftpd
- Restart the vsftpd service <br>
    `sudo service vsftpd restart`

---

### Ensure SSH is Installed
- for Ubuntu <br>
    `sudo apt-get install openssh-server`

---

### Configure SSH for FTP User
- Ensure the FTP user has SSH access. Eidt the SSH Daemon configuration file. <br>
    `sudo nano /etc/ssh/sshd_config`
    - Ensure the line is present (uncomment): <br>
        `Subsystem sftp internal-sftp`

---

### Restart SSH
- restart the SSH Service <br>
    `sudo service ssh restart`

  <p>With either option, FTP Communication will be secured using encryption. Choose the option that best fits your requirements and network environment.</p>
  <p>Keep in mind that SFTP is more modern and secure choice, as it integrates with the existing SSH infrastructure</p>  

---

### Explicit FTPS
1. Using FTP Client:
    - Use an FTP Client that support `Explicit` FTPS
2. Configure FTP Client:
    - Enter FTP Host/Server Address, port (default is 21), and FTP User Credentials.
    - Choose `FTPES` or `Explicit FTPS` as the encription method.
3. Connect:
    - Connect to the FTP Server. The client and erver will negotiate the secure connection.

---

### SFTP <br>
1. Using SFTP Client
    - Use an SFTP Client
2. Configure SFTP Client:
    - Enter FTP Host/Server, port (default is 22), and FTP User Credentials.
3. Connect:
    - Connect to the FTP Server. SFTP operates over the SSH Protocol, and the connection will be secured.

---

- [x] For Explicit FTPS, default FTP Port is `21` and default FTPS port is usually `990`.
- [x] For SFTP, the default SSH port is `22`.
- [x] Certificate Verification: prompts you to accept the certificate. It's importatnt to verify the server's identity for security reasons.
- [x] User Authentication: Ensure that FTP user credentials are valid for authentication.
- [x] Firewall Considerations: If your have a firewall, make sure the necessary ports (FTP is `21` and FTPS is `990`, or SFTP is `21`)

### Configure Firewall (Optional)
```
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 40000:50000/tcp
sudo ufw allow 990/tcp
sudo ufw allow openssh
sudo ufw enable
sudo ufw status
```

### Additional Configuration
- `vsfptd.conf` additional configuration
```
force_dot_files=YES
pasv_min_port=400000
pasv_max_port=500000
user_sub_token=$USER
local_root=/home/$USER/ftp
```

### Restart `vsftpd.conf` to have changes take effect
    `sudo systemctl restart vsftpd.service`