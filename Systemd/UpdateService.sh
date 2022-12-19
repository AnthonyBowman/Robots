systemctl stop $1 
systemctl disable $1
cp $1 /lib/systemd/system
chmod 644 /lib/systemd/system/$1
systemctl daemon-reload
systemctl enable $1
systemctl start $1
