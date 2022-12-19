cp StreamServer.service /lib/systemd/system/StreamServer.service
chmod 644 /lib/systemd/system/StreamServer.service
cp UMC.service /lib/systemd/system/UMC.service
chmod 644 /lib/systemd/system/UMC.service
systemctl daemon-reload
