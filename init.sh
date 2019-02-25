#mkdir -p /home/box/web/uploads /home/box/web/public/img  /home/box/web/public/css /home/box/web/public/js
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
cd /home/box/web/etc/
gunicorn -w 4 --bind 127.0.0.1:8080 hello:app
#sudo /etc/init.d/mysql start

