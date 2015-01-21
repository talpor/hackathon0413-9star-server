#! /bin/sh

### BEGIN INIT INFO
# Provides:          9star server
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the 9star web server
# Description:       starts 9star using start-stop-daemon
### END INIT INFO

# /etc/init.d/9star
#

case "$1" in
  start)
    echo "Starting 9star server"
    cd /home/pi/9star/ && /usr/local/bin/gunicorn --pythonpath="NineStarServer" wsgi:application -c gunicorn.conf.py &
    ;;
  stop)
    echo "Stopping 9star server"
    pkill gunicorn
    ;;
  *)
    echo "Usage: /etc/init.d/9star {start|stop}"
    exit 1
    ;;
esac

exit 0
