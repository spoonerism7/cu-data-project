from ftplib import FTP
import os

def download_files_from_ftp(host, port, username, password, remote_dir, local_dir):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(user=username, passwd=password)

    ftp.cwd(remote_dir)

    os.makedirs(local_dir, exist_ok=True)

    files = ftp.nlst()

    downloaded_files = []

    for file_name in files:
        local_path = os.path.join(local_dir, file_name)

        with open(local_path, "wb") as f:
            ftp.retrbinary(f"RETR {file_name}", f.write)

        downloaded_files.append(local_path)

    ftp.quit()

    return downloaded_files