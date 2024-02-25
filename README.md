
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

- [ ] ftp connection successful
- [ ] add configuration `etc/vsftpd.conf`
    - [ ] force_local_logins_ssl=NO
    - [ ] force_local_data_ssl=NO

- [x] unregister unix distro in WSL (Ubuntu)
- [x] reinstall again Ubuntu, install `vsftpd`, add `ftpuser`, configuration `/etc/vsftpd.conf`
- [x] remove `userprofile\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu*` from local machine
- [x] (optional) `userprofile\AppData\Local\Microsoft\Windows\WSL\`
- [x] adds permission to ftpuser to create CSV file to `ftp` folder
        - directory: `/home/ftpuser/ftp`
- [ ] owner: `nobody`
- [ ] group: `nogroup`
- [ ] permission: `drwxr-xr-x` (read, write and execute for the owner, and read/excure for group and others)
- [x] allow the FTP User `ftpuser` to upload files:
    - [x] change owmership of the directory to `ftpuser`:
        `sudo chown ftpuser:ftpuser /home/ftpuser/ftp`
    - [x] add the ftpuser to the group `nogroup`:
        `sudo usermod -aG nogroup ftpuser`
    - [x] allow the owner (nobody) to write to the directory:
        `sudo chmod u+w /home/ftpuser/ftp`
