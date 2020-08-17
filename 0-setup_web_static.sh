#!/usr/bin/env bash
# bash script that sets up your web servers for the deployment
if ! which nginx > /dev/null; then
	sudo apt -y update
	sudo apt -y upgrade
	sudo apt install nginx
fi
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu: /data/
sudo sed -i "55i\\tlocation hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sudo service nginx restart
