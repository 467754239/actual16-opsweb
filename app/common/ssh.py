


import paramiko




def execute_command_for_password(hostname, username, password, cmd, port=22):
    '''
        http://blog.51cto.com/467754239/1619166
    '''
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(cmd)
    return stdout.read()



def execute_upload_for_passwd(host, username, password, localFile, remoteFile, port=22):
    s = paramiko.Transport((host, port))
    s.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(s)
    sftp.put(localFile, remoteFile)
    s.close()




if __name__ == '__main__':
    pass
