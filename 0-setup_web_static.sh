#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static
echo "Updating dependencies..."
sudo apt-get -y update
sleep 2
echo "Installing nginx..."
sudo apt-get -y install nginx
sleep 2
echo "Setting up file structure..."
sudo mkdir -p '/data/'
sudo mkdir -p '/data/webstatic/'
sudo mkdir -p '/data/web_static/releases/'
sudo mkdir -p '/data/web_static/shared/'
sudo mkdir -p '/data/web_static/releases/test/'
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee '/data/web_static/releases/test/index.html'
sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'
sudo chown -R ubuntu:ubuntu '/data/'
sleep 2
echo "Configuring nginx..."
echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html
echo "server {
    listen 80;
    listen [::]:80;
    error_page 404 /custom_404.html;
    add_header X-Served-By $HOSTNAME;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=o_oenl2Be-w;
    }

    location /custom_404.html {
        root /var/www/html;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        autoindex off;
    }
}" | sudo tee /etc/nginx/sites-available/default
sleep 2
echo "Restarting nginx..."
sudo service nginx restart
sleep 2
