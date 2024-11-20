# mail_ai_gen
Gen AI, FastAPI

**Reference**
- [FastAPI Production setup](https://github.com/Antony-M1/fastapi-production-setup/blob/main/production-setup.md)
- [Deploy FastAPI on AWS EC2: Quick and Easy Steps!](https://medium.com/@shreyash966977/deploy-fastapi-on-aws-ec2-quick-and-easy-steps-954d4a1e4742)

# Production Setup

For the production setup please ensure that the `.pem` has correct permissions
```
chmod 600 <YOUR_PEM_FILE>
```

<details>
  <summary><h3>Production Setup Command</h3></summary>


```sh
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/mail_ai_gen
ExecStart=/home/ubuntu/mail_ai_gen/venv/bin/gunicorn \
          --access-logfile - \
          --workers 5 \
          --bind unix:/run/gunicorn.sock \
          --worker-class uvicorn.workers.UvicornWorker \
          main:app

[Install]
WantedBy=multi-user.target



sudo nano /etc/nginx/sites-available/mail_ai_gen

vivantai.softsuavetestandpocs.in

server {
    listen 80;
    server_name vivantai.softsuavetestandpocs.in;
    location / {
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/mail_ai_gen /etc/nginx/sites-enabled

# Certbot
sudo apt install certbot python3-certbot-nginx -y

sudo certbot --nginx -d vivantai.softsuavetestandpocs.in

```
</details>