import subprocess as sub
import time
import random
def new_mac():#function for creating new MAC addresss
    mac=[]
    l=''
    for i in range(0,6):
        if i==0:
            x=random.randrange(16,200,2)#Giving Random number, remember first octet of MAC is always keep even number
            l=hex(x).lstrip('0x')#Striping 0x from hex number
            mac.append(l)
        else:
            x=random.randrange(16,200)#For random number
            l=hex(x).lstrip('0x')
            mac.append(l)
    a,b,c,d,e,f=mac# Mapping list 
    mac='{}:{}:{}:{}:{}:{}'.format(a,b,c,d,e,f)#formating MAC address
    return mac#Returning MAC address
def interface_name():#function for taking interface name from user
    flag=0
    while flag==0:#For input validation
        i=input('Please enter interface name: ')
        error=sub.run(['ifconfig',i],capture_output=True)#Checking user input is valid or not 
        if error.returncode!=0:
            print('Please enter valid device name')
            flag=0
        else:
            return i
            flag=1
def mac_change(interface,mac):# function for changing mac
    sub.run(['ifconfig',interface, 'down'])#Command for turning down network. Running linux commands using subprocess library
    sub.run(['ifconfig',interface,'hw','ether',mac])#Command for changing MAC address
    sub.run(['ifconfig',interface,'up'])#Command for turning up network
    
    
print('********Welcome to Mac_changer********')
print('Warning: script will change your mac address after every 60 seconds.')
print('To exit please press ctrl c.')

if __name__=='__main__':
    interface=interface_name()
    while(1):#Changing MAC address after every 60 seconds
        mac=new_mac()
        mac_change(interface,mac)
        print('Successfully mac changed')
        time.sleep(60)#For delay of 60 seconds
        

