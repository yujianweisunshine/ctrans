from ftplib import FTP

class domain:
    def __init__(self, host, port, name, passwd):
        try:
            self.ftp = FTP()
            ftp.connect(host, port, 3) 
            ftp.login(name, passwd)
        except :
            print("host error")

    def downfile(self, filename):
        try:
            print("donwfile....")
        except expression as identifier:
            pass 



if __name__ == "__main__":
    ip = "192.168.1.111"
    port = 21
    name = 
    passwd = 
    tfp = domain(ip, port, name ,passwd)
    tfp.downfile()