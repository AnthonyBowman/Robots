#!/bin/bash 

# Raspberry Pi - bookwoom - robot builder

# ensure latest operating system
sudo apt update
sudo apt upgrade

# ---- Install TigerVNC ---- 
sudo apt install tigervnc-standalone-server

# Set VNC password
vncpasswd 

# Configure systemd service for TigerVNC under Wayland
sudo tee /etc/systemd/system/vncserver@.service <<END
[Unit]
Description=Remote desktop service (VNC)
After=syslog.target network.target

[Service]
Type=simple
User=pi
PAMName=login
PIDFile=/home/%i/.vnc/%H%i.pid
ExecStartPre=-/usr/bin/vncserver -kill :%i > /dev/null 2>&1
ExecStart=/usr/bin/vncserver -depth 24 -geometry 1280x800 :%i
ExecStop=/usr/bin/vncserver -kill :%i

[Install]  
WantedBy=multi-user.target
END

# Enable the service
sudo systemctl enable vncserver@1.service

----- Install Git and clone ----

# Prompt for repository choice
echo "Select repository to clone:"
select repo in Robots Routers
do
  case $repo in
    Robots)
      git_repo="https://github.com/AnthonyBowman/Robots.git"
      target_dir="Robots"
      break
      ;;
    Routers)  
      git_repo="https://github.com/AnthonyBowman/Routers.git"
      target_dir="Routers"
      break
      ;;
  esac
done

# Actuall install git
sudo apt update
sudo apt install git

# Add pi user to git group to avoid needing sudo 
sudo usermod -aG git pi
git config --global user.name "AnthonyBowman"
git config --global user.email "brian@sherr.co.uk


# Clone selected repository
git clone $git_repo $target_dir

# After git clone

if [ "$repo" = "Robots" ]; then

  # Push Systemd directory
  pushd $target_dir/Systemd

  # Run install script
  bash InstallServices.sh
  
  # Run enable script
  bash EnableServices.sh

  # Return to original directory
  popd

fi

---- Optionally install Mosquitto ----

# Ask if user wants to install Mosquitto
read -p "Install Mosquitto MQTT? (y/n) " install_mosquitto

# Check response
if [ "$install_mosquitto" = "y" ]; then

  # Install Mosquitto
  sudo apt update
  sudo apt install -y mosquitto mosquitto-clients
  
  # Configure Mosquitto
  sudo mosquitto_passwd -c /etc/mosquitto/passwd username
  sudo chown mosquitto:mosquitto /etc/mosquitto/passwd

  # Update config 
  echo "allow_anonymous false" | sudo tee -a /etc/mosquitto/mosquitto.conf
  echo "password_file /etc/mosquitto/passwd" | sudo tee -a /etc/mosquitto/mosquitto.conf

  # Enable and restart service
  sudo systemctl enable mosquitto.service 
  sudo systemctl restart mosquitto.service

fi

---- Install OpenCV ----
# Install OpenCV dependencies
sudo apt update 
sudo apt install -y libopencv-dev python3-opencv

# Also install useful utils
sudo apt install -y libjpeg-dev libpng-dev libtiff-dev 

# Clean up cache
sudo apt clean

---- Setup Known Wifi ----

# Prompt to add networks
read -p "Add known WiFi networks? (y/n) " add_wifi

if [ "$add_wifi" = "y" ]; then

  # Network 1
  ssid="CrossBow"
  psk="loblocks13"

  echo "Adding $ssid..."
  nmcli connection add con-name "$ssid" ifname wlan0 type wifi ssid "$ssid" 
  nmcli connection modify "$ssid" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "$psk"

  # Network 3
  ssid="PiLab"
  psk="Raspberry13"

  echo "Adding $ssid..."
  nmcli connection add con-name "$ssid" ifname wlan0 type wifi ssid "$ssid"
  nmcli connection modify "$ssid" wifi-sec.key-mgmt wpa-psk wifi-sec.psk "$psk"
  
fi