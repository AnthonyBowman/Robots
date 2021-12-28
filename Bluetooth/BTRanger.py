import blescan
import bluetooth._bluetooth as bluez
from Tkinter import *

top = Tk()
average = 0
count = 0

def get_distance (txpower, rssi):
    PL0 = txpower - rssi
    return pow(10, ((txpower - rssi - PL0)) / (10 * 2));
    
def calculate_accuracy(txpower, rssi):
    if rssi == 0 or txpower == 0:
        return -1
    else:
        ratio = rssi/txpower
        if ratio < 1:
            return ratio**10
        else:
            return 0.89976 * ratio**7.7095 + 0.111
 
 
def scan_sock(sock, top):
    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)
     
    returnedList = blescan.parse_events(sock, 10)

    global count
    global average
    print "----------", count, average

    
    for beacon in returnedList:
        beacon = beacon.split(',')
        bluetoothAddress = beacon[0]
        beaconid = beacon[1]
        major = beacon[2]
        minor = beacon[3]
        txpower = float(beacon[4])
        rssi = float(beacon[5])
 
        if beaconid.upper() == "10F86430134611E491910800200C9A66": #"6B55FCD87A8146B38928D245813EBAA1":
            print "found our beacon", bluetoothAddress, "id= ", beaconid, "\nmajor=", major, "minor=", minor, "\ntxpower=", txpower, "rssi=", rssi
            distance = calculate_accuracy(txpower, rssi)
            messageOur = "dist=" + str(distance)
            messageVar = Message(top, text=messageOur, width=250)
            messageVar.place(x=5,y=50)
 
            average = average + distance 
            count = count + 1
            if count > 12:
                average = average / count
                messageOur = "average=" + str(average)
                messageVar1 = Message(top, text=messageOur, width=250)
                messageVar1.place(x=5,y=100) 
                count = 0
                
    top.after(2000, scan_sock, sock, top)
 
if __name__ == '__main__':
    dev_id = 0
        
    # Code to add widgets will go here...

    #try:
    sock = bluez.hci_open_dev(dev_id)
    print "ble thread started"
    #scan_sock(sock)
    #except:
    #    print "error accessing bluetooth device..."

messageVar = Message(top, text="hello", width=250)
messageVar.pack()
top.after(2000, scan_sock, sock, top)
top.mainloop()
    
  
