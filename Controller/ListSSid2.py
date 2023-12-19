import subprocess

def list_available_ssids(interface):
    command = f"sudo iwlist {interface} scan | grep ESSID"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    ssids = [line.split(":")[1].strip().strip('"') for line in output.split("\n") if "ESSID:" in line]
    ssids = [ssid for ssid in ssids if ssid and not ssid.isspace()]
    return ssids

if __name__ == "__main__":
    interface = "wlan1"
    ssids = list_available_ssids(interface)
    print("Available SSIDs:")
    for ssid in ssids:
        print(ssid)
