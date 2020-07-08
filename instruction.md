## Create a service
`sudo nano /lib/systemd/system/WifiConnector.service`
### Add the following to the file
    [Unit]
    Description = A Service that uses QR Reader to connect to Wifi
    After=multi-user.target
    
    [Service]
    Type=idle
    ExecStart = /usr/bin/python /path/to/WifiConnector.py

    [Install]
    WantedBy=multi-user.target

### If you want to log
Change the ExecStart line to
    
    ExecStart=/usr/bin/python /path/to/WifiConnector.py > /home/pi/sample.log 2>&1

### Add permision
`sudo chmod 644 /lib/systemd/system/WifiConnector.service`

## Configure systemd
    sudo systemctl daemon-reload

    sudo systemctl enable WifiConnector.service

### Reboot
    sudo reboot