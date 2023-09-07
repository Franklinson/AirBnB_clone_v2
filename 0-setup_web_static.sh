#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

echo "<html>
  <head></head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

nginx_config="/etc/nginx/sites-available/default"
nginx_alias="location /hbnb_static/ {\n    alias /data/web_static/current/;\n}\n"

if ! grep -q "location /hbnb_static/" "$nginx_config"; then
    sudo sed -i "/server_name _;/a $nginx_alias" "$nginx_config"
fi

sudo service nginx restart
