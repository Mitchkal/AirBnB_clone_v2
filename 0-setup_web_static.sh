#!/usr/bin/env bash
#sets up web servers for web_static deployment

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "<html><head></head><body><p>Hello Kitty, this is nginx</p></body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

static_block="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup
sudo sed -i "49i $static_block" /etc/nginx/sites-available/default
sudo service nginx start
