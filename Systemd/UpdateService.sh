systemctl stop $1 
cp $1 /lib/systemd/system
systemctl daemon-reload
systemctl start $1
