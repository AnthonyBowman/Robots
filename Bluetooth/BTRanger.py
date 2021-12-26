import blescan
import bluetooth._bluetooth as bluez
 
 
def calculate_accuracy(txpower, rssi):
    if rssi == 0 or txpower == 0:
        return -1
    else:
        ratio = rssi/txpower
        if ratio < 1:
            return ratio**10
        else:
            return 0.89976 * ratio**7.7095 + 0.111
 
 
def scan_sock(sock):
    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)
     
    while True:
        returnedList = blescan.parse_events(sock, 10)
        print "----------"
        for beacon in returnedList:
            print beacon
            beacon = beacon.split(',')
            beaconid = beacon[0]
            txpower = float(beacon[4])
            rssi = float(beacon[5])
            if 0<= calculate_accuracy(txpower, rssi):
                print beaconid
 
if __name__ == '__main__':
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"
        scan(sock)
    except:
        print "error accessing bluetooth device..."