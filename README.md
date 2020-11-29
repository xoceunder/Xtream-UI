# Install Xtream-UI R24 on Ubuntu 18.04 Server
Here you can read how to instal XtreamUI R24 on a Ubuntu 18.04 Server

# 1.Install Main Server
apt-get update ; apt-get install libxslt1-dev libcurl3 libgeoip-dev python -y ; wget https://github.com/xoceunder/Xtream-UI/raw/master/install.py ; sudo python install.py

# 2.Update XtreamUI
apt-get install unzip e2fsprogs python-paramiko -y && chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && rm -rf /home/xtreamcodes/iptv_xtream_codes/admin && rm -rf /home/xtreamcodes/iptv_xtream_codes/pytools && wget "https://www.dropbox.com/s/azubd6jfdk87d64/update.zip?dl=0" -O /tmp/update.zip -o /dev/null && unzip /tmp/update.zip -d /tmp/update/ && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ && rm -rf /tmp/update/XtreamUI-master && rm /tmp/update.zip && rm -rf /tmp/update && chattr +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ && /home/xtreamcodes/iptv_xtream_codes/start_services.sh

# 3.GeoLite2.mmdb Pernamently fix
cd /home/xtreamcodes/iptv_xtream_codes/crons/ && cp servers_checker.php servers_checker.php.orgi && rm servers_checker.php && wget https://www.dropbox.com/s/6gnof4z1v3jw5hb/servers_checker.php?dl=0 && sudo chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && sudo chmod 777 /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && sudo chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ && sudo chmod 777 -R /home/xtreamcodes/iptv_xtream_codes/crons && sudo /home/xtreamcodes/iptv_xtream_codes/start_services.sh

# 4.Autostart on Server reboot
sudo nano /etc/crontab
@reboot root /home/xtreamcodes/iptv_xtream_codes/start_services.sh

# 5.PID Monitor Fix
wget "https://www.dropbox.com/s/hlqhah77dgpx99d/pid_monitor.zip?dl=0" -O /tmp/pid_monitor.zip -o /dev/null && unzip /tmp/pid_monitor.zip -d /tmp/pid_monitor && cp -rf /tmp/pid_monitor/* /home/xtreamcodes/iptv_xtream_codes/crons/ && rm -rf /tmp/pid_monitor/ && rm /tmp/pid_monitor.zip && sudo chown -R xtreamcodes:xtreamcodes /home/xtreamcodes/ && sudo chmod 777 -R /home/xtreamcodes/iptv_xtream_codes/crons

# 6.Login with User: admin and Psaaword: admin

# 7.Go to Panel Settings > Backups > Update Tables
