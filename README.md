### Enable Virtual Machine Platform for WSL
- WSL2 requires the Virtual Marchine Platform feature. Ruth the following command in Powershell: <br>
    `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
---
### Checking WSL Version
- Open Powershell and run the command: <br>
    `wsl --list --verbose` <br>
    *This command will list the installed WSL Distributions along with their versions.*
---
### Check Installed Distributions
- Open Powershell and run the command: <br>
    `wsl --list` <br>
    *If you see any distribution names, WSL is installed, and you'll see the available distributions.*
---
### Install Ubuntu
- Open Powershell and run the command: <br>
    `wsl --install -d Ubuntu` <br>
    *Wait for a few minutes to process the installation of distribution.*
---
### Create Ubuntu Root Account
- When you first install Ubuntu on WSL, it typically prompts you to create a new user and set a password during initial setup. This user is granded sudo privileges, allowing you to perform administrative tasks.
---
### Update and Upgrade Pacakges:
- Open the Ubuntu terminal and run the following command to update the packages lists and upgrade installed packages (`-y` means yes to installation):
    `sudo apt update && apt upgrade -y`
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
--- 
### Change user to Root Access (Administrative Access)
- This may helpful to install packages without putting password everytime the installation required.
    `sudo su - ` <br>
    - apply the password to continue
---
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
    ```
    ssl_enable=YES
    allow_anon_ssl=NO
    force_local_data_ssl=NO
    force_local_logins_ssl=NO
    ``` 
    <br>
    
    `ssl_enable=YES` means transport Layer Security is enable to FTP server. <br>
    `allow_anon_ssl=NO` means users without username/password cannot use SSL for encription. <br>
    `force_local_data_ssl=NO` means whether SSL is required for local upload nad downloads, it's not mandatory for local data transfer. <br>
    `force_local_logins_ssl=NO` means whether SSL is required for local logins, it's not mandatory for local logins.
---
### Restart vsftpd services
- restart the vsftpd service <br>
    `sudo systemctl restart vsftpd`
---    
### Checking vsftpd services
- check the vsftpd service status <br>
    `sudo systemctl status vsftpd` <br>
    *Active: active (running) since Day YYYY-MM-DD hh:mm:ss +08; --h --min ago ...* 
