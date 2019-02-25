<<<<<<< HEAD
mkdir -p /home/box/web/uploads /home/box/web/public/img  /home/box/web/public/css /home/box/web/public/js
=======
>>>>>>> ce3e51b4166391f8de94a023f3a36c8871b44c5b
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start

