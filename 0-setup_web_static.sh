#!/usr/bin/env bash
# This script will set up our web server for deployment of web_static.

# -- Update & Nginx Installation
sudo apt-get update -y
sudo apt-get install nginx -y

# This will create our folders (-p option creates intermediate directories)
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Using echo and tee we will create a fake html file to test Nginx config
# echo -e enables backslash interpretation (for our newlines to be recognized)
# sudo tee will read from standard input and write to STDOUT
echo -e "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>\n" | sudo tee /data/web_static/releases/test/index.html

# This will create a symbolic link linking /data/web_static/current to
# data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# This will give ownership of /data/ folder to ubuntu user & group recursively
sudo chown -R ubuntu:ubuntu /data/

# This will update our Nginx configuration to serve content of
# /data/web_static/current/ to hbnb_static
sudo sed -i "48i location /hbnb_static {\nalias /data/web_static/current/;\n}" /etc/nginx/sites-enabled/default

# This will restart our Nginx after updating the configuration.
sudo service nginx restart
