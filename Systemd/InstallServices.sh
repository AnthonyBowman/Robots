cp StreamServer.service /lib/systemd/system/StreamServer.service
chmod 644 /lib/systemd/system/StreamServer.service
cp UMC.service /lib/systemd/system/UMC.service
chmod 644 /lib/systemd/system/UMC.service
cp USC.service /lib/systemd/system/USC.service
chmod 644 /lib/systemd/system/USC.service
cp ObstacleAvoidance.service /lib/systemd/system/ObstacleAvoidance.service
chmod 644 /lib/systemd/system/ObstacleAvoidance.service
systemctl daemon-reload
