#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if ! test -f nginx; then
	sudo apt -y update
	sudo apt -y upgrade
	sudo apt -y install nginx
fi

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
content="Holberton school"
echo "$content" > /data/web_static/releases/test/index.html
if test -L /data/web_static/current; then
	rm -rf /data/web_static/current
	ln -sf /data/web_static/releases/test/ /data/web_static/current
else
	ln -sf /data/web_static/releases/test/ /data/web_static/current
fi;
sudo chown -hR ubuntu:/data
sudo sed -i '55i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
