import assets.python.Global as Global
import paramiko
import os 

class Connect:
	def __init__(self):
		self.ssh = None
		self.sftp = None 
		self.transport = None
		self.sShconnect()
	def sShconnect(self):

		paramiko.util.log_to_file('paramiko.log')  # build a log file for watch log
		self.ssh = paramiko.SSHClient()  
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # use public to check	
		self.ssh.connect(Global.SERVERIP,username = Global.SERVERNAME,pkey=paramiko.RSAKey.from_private_key_file(Global.SERVERKEY)) # pkey = private key
		# stdin,stdout,srderr = ssh.exec_command("cd "+Global.SERVERADDRESS+" && ls -1 | wc -l")
		# dirfilecounts = stdout.read().rstrip()

		return self.ssh

	def sShclose(self):
		self.ssh.close()
	
	def sFtpconnect(self):
		self.transport = paramiko.Transport((Global.SERVERIP,Global.SERVERPORT))
		self.transport.connect(username = Global.SERVERNAME,pkey =paramiko.RSAKey.from_private_key_file(Global.SERVERKEY))
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)

	def sFtpput(self,file="."):
		return self.sftp.put(Global.ADDRESS+"/"+file,Global.SERVERADDRESS+"/"+file)
	
	def sFtplistdir(self):
		return self.sftp.listdir(Global.SERVERADDRESS)

	def sFtpremove(self,file="."):
		return self.sftp.remove(Global.SERVERADDRESS+"/"+file)

	def sFtpclose(self):
		self.sftp.close()
	