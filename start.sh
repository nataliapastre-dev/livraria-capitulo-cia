#!/bin/bash
set -e

pip install -r requirements.txt



NGINX_CONF="/etc/nginx/sites-available/livraria"
PROJECT_PATH="/var/www/livraria"

sudo bash -c "cat > $NGINX_CONF" <<EOF
server {
    listen 80;
    server_name _;

    location /static/ {
        alias $PROJECT_PATH/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

sudo ln -sf $NGINX_CONF /etc/nginx/sites-enabled/

sudo nginx -t

