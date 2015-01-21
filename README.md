hackathon0413-9star-server
==========================

* Install requirements as root.
* Run::
    [sudo] gunicorn --pythonpath="NineStarServer" wsgi:application -c gunicorn.conf.py
* Symlink /etc/nginx/sites-enabled/9star.conf -> nginx.conf and restart nginx.
* If you want an init script::
  + Symlink /etc/init.d/9star -> 9star.sh
  + chmod +x /etc/init.d/9star
  + update-rc.d 9star defaults

Sit back and enjoy =).
