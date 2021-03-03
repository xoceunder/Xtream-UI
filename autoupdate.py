#!/usr/bin/python
# -*- coding: utf-8 -*-
# update panel
import subprocess, os, random, string, sys, shutil, socket, zipfile, urllib2
from itertools import cycle, izip
from zipfile import ZipFile
from urllib2 import Request, urlopen, URLError, HTTPError

def autoupdate():
    rNginx = "/home/xtreamcodes/iptv_xtream_codes/nginx/conf/nginx.conf"
    rNginxRtmp = "/home/xtreamcodes/iptv_xtream_codes/nginx_rtmp/conf/nginx.conf"
    rIni = "/home/xtreamcodes/iptv_xtream_codes/php/lib/php.ini"
    rIsp = "/home/xtreamcodes/iptv_xtream_codes/wwwdir/includes/streaming.php"
    os.system("rm /home/xtreamcodes/iptv_xtream_codes/adtools/backups/* 2>/dev/null")
    os.system('mv "%s" "%s.xc" && mv "%s" "%s.xc" && mv "%s" "%s.xc" && mv "%s" "%s.xc"' % (rNginx, rNginx, rNginxRtmp, rNginxRtmp, rIni, rIni, rIsp, rIsp))
    os.system('chattr -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && wget "https://github.com/xoceunder/Xtream-UI/raw/master/update.zip" -O /tmp/update.zip -o /dev/null && unzip /tmp/update.zip -d /tmp/update/ >/dev/null && rm -rf /home/xtreamcodes/iptv_xtream_codes/crons && rm -rf /home/xtreamcodes/iptv_xtream_codes/php/etc && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ 2>/dev/null && rm -rf /tmp/update/XtreamUI-master && rm /tmp/update.zip && rm -rf /tmp/update && wget https://github.com/xoceunder/Xtream-UI/raw/master/GeoLite2.mmdb -O /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb -o /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes && find /home/xtreamcodes/ -type d -not \( -name .update -prune \) -exec chmod -R 777 {} + && chattr +i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb && rm /usr/bin/ffmpeg 2>/dev/null || rm /usr/bin/ffprobe 2>/dev/null || ln -s /home/xtreamcodes/iptv_xtream_codes/bin/ffmpeg /usr/bin/')
    os.system('mv "%s.xc" "%s" && mv "%s.xc" "%s" && mv "%s.xc" "%s" && mv "%s.xc" "%s"' % (rNginx, rNginx, rNginxRtmp, rNginxRtmp, rIni, rIni, rIsp, rIsp))
    return True

def start():
    os.system("/home/xtreamcodes/iptv_xtream_codes/start_services.sh 2>/dev/null")
    return True

if __name__ == "__main__":
    autoupdate()
    start()