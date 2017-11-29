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
		# connect to server 
		paramiko.util.log_to_file('paramiko.log')  # build a log file for watch log
		self.ssh = paramiko.SSHClient()  
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # use public to check	
		self.ssh.connect(Global.SERVERIP,username = Global.SERVERNAME,pkey=paramiko.RSAKey.from_private_key_file(Global.SERVERKEY)) # pkey = private key
		
		return self

	def sShexeccommand(self,command=""):
		stdin,stdout,stderr = self.ssh.exec_command(command)
		print(stdout.readlines())
		return self
	def sShclose(self):
		self.ssh.close()
		return self
	
	def sFtpconnect(self):
		self.transport = paramiko.Transport((Global.SERVERIP,Global.SERVERPORT))
		self.transport.connect(username = Global.SERVERNAME,pkey =paramiko.RSAKey.from_private_key_file(Global.SERVERKEY))
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)
		return self

	def sFtpput(self,file="."):
		self.sftp.put(Global.ADDRESS+"/"+file,Global.SERVERADDRESS+"/data/"+file)
		return self
	
	def sFtplistdir(self):
		return self.sftp.listdir(Global.SERVERADDRESS+"/data")

	def sFtpremove(self,file="."):
		self.sftp.remove(Global.SERVERADDRESS+"/data/"+file)
		return self

	def sFtpclose(self):
		self.sftp.close()
		return self
	