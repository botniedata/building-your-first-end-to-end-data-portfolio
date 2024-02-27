
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

### Provide Ownership of Directory 
- This command provides ownership of the directory `/home/<user>/ftp` to the user and group `ftpuser`
    `sudo chown ftpuser:ftpuser /home/ftpuser/ftp`

---

### Add the user `ftpuser` to the `nogroup`
- Using `usermod` to add the user `ftpuser` to the `nogroup` group.
    `sudo usermod -aG nogroup ftpuser`

---

### Add `write` permission for the user `ftpuser`
- Using `chmod` to tadd write permission for the owner of the directory `/home/ftpuser/fpt`.
    `sudo chmod u+w /home/ftpuser/ftp`

---

### Check OpenSSL Version:
- Open terminal and run the command:
    `openssl version`

---    

### Check OpenSSL Package Installation:
- On Linux system you can use a package manager to check if OpenSSL is installed:
    `dpkg -l | grep openssl`

---    

### Check OpenSSL Executable:
- Check OpenSSL executable is present on your system. Typical location is `/usr/bin/openssl`:
    `ls /usr/bin/openssl`

---

### Install vsftpd
- Ensure that `vsftpd` (Very Secure FTP Daemon) is installed on your system. You can use your package manager to install:
    `sudo apt-get install vsftpd`

--- 

### Configure vsftpd
- Open the `vsftpd.conf` file in a text editor (usually located in `/etc/vsftpd.conf`).
    `sudo nano /etc/vsftpd.conf`
    - Ensure the following lines are set (uncomment):
    ```ssl_enable=YES
    allow_anon_ssl=NO
    force_local_data_ssl=YES
    force_local_logins_ssl=YES
    ``` 
---

### Generate SSL Certificate:
- Generate a self-signed SSL certificate for FTP:
    `sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.pem -out /etc/ssl/private/vsftpd.pem`

---

### Restart vsftpd
- Restart the vsftpd service
    `sudo service vsftpd restart`

---

### Ensure SSH is Installed:
- for Ubuntu
    `sudo apt-get install openssh-server`

---

### Configure SSH for FTP User:
- Ensure the FTP user has SSH access. Eidt the SSH Daemon configuration file.
    `sudo nano /etc/ssh/sshd_config`
    - Ensure the line is present (uncomment):
        `Subsystem sftp internal-sftp`

---

### Restart SSH
- restart the SSH Service
    `sudo service ssh restart`

  <p>With either option, FTP Communication will be secured using encryption. Choose the option that best fits your requirements and network environment.</p>
  <p>Keep in mind that SFTP is more modern and secure choice, as it integrates with the existing SSH infrastructure</p>  
