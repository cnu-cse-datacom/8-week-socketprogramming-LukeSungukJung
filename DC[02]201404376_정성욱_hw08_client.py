import socket
import numpy as np


ip_addr = "192.168.60.135"
port = "9000"
file_name = input("Input your file name :")

print("File Transmit Start....")

socket =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss =  open(file_name,'rb')
data = ss.read().hex()
data_tranfer_coeff = 0
file_size = len(data)
socket.sendto(file_name.encode(),(ip_addr,int(port)))

rp_number =file_size/1024
if(rp_number-np.floor(rp_number)>0):
    rp_number=  (np.floor(rp_number)+1) 
else :
    rp_number=  np.floor(rp_number)

socket.sendto(str(file_size).encode(),(ip_addr,int(port)))
count =1;


while(count<=rp_number):            
    print(count,"th send")
    if ((file_size-data_tranfer_coeff)>=1024):
        send_to_dgram = data[data_tranfer_coeff:data_tranfer_coeff+1024]
        socket.sendto(send_to_dgram.encode(),(ip_addr,int(port)))
        print("current_size / total_size =",count*1024,"/",file_size,count*1024/file_size*100)
    else:
        send_to_dgram = data[data_tranfer_coeff:data_tranfer_coeff+(file_size-data_tranfer_coeff)]
        socket.sendto(send_to_dgram.encode(),(ip_addr,int(port)))
        print("current_size / total_size =",(count-1)*1024+(file_size-data_tranfer_coeff),"/",file_size,((count-1)*1024+(file_size-data_tranfer_coeff))/file_size*100)
        break;
    count= count+1
    data_tranfer_coeff= data_tranfer_coeff+1024
    
print("ok")
print("file_send_end")

    
    
    
