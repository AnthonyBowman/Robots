import pywifi

def list_available_ssids(interface):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[interface]
    iface.scan()
    ssids = [network.ssid for network in iface.scan_results() if network.ssid]
    return ssids

if __name__ == "__main__":
    interface = 0  # Replace with the index of the desired interface (e.g., 0 for wlan0)
    ssids = list_available_ssids(interface)
    print("Available SSIDs:")
    for ssid in ssids:
        print(ssid)
