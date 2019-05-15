import socket
import numpy as np


server_socket  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.settimeout(10)
server_socket.bind(('',9000))

filename,addr = server_socket.recvfrom(100)
from_place = addr[0]

print("file recv start from ",from_place)
print(filename)
fileName = filename.decode()
print("File Name: ",fileName)

filesize,_ = server_socket.recvfrom(100)
filesize = int(filesize.decode())
print("File size: ",filesize)

rp_number = float(filesize)/1024

if(rp_number-np.floor(rp_number)>0):
    rp_number=  (np.floor(rp_number)+1) 
else :
    rp_number=  np.floor(rp_number)
 
print(rp_number)
data_tranfer_coeff = 0
recv_count =1

recv_list = []

while(recv_count<=rp_number):
    try:
        if ((filesize-data_tranfer_coeff)>=1024): 
            data,_ = server_socket.recvfrom(1024)
                
            recv_list.append(data.decode()) 
            print("current_size / total_size =",recv_count*1024,"/",filesize,recv_count*1024/filesize*100)
        else:
            data,_ = server_socket.recvfrom(filesize-data_tranfer_coeff)
            recv_list.append(data.decode()) 
            print("current_size / total_size =",(recv_count-1)*1024+(filesize-data_tranfer_coeff),"/",filesize,((recv_count-1)*1024+(filesize-data_tranfer_coeff))/filesize*100)
            
        data_tranfer_coeff= data_tranfer_coeff+1024
        recv_count= recv_count+1
    except socket.timeout:
        break

recv_data=bytes.fromhex(''.join(recv_list))

recv_file = open(filename,'wb')
recv_file.write(recv_data)
recv_file.close()
#server_socket.sendto("hello client".encode(),addr)


