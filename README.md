# OpsWeb Platform

- [x] flask
- [x] mysql
- [x] redis
- [x] bootstrap
- [x] paramiko
- [x] echarts 



# Deploy
> flask + nginx + uwsgi + virtualenv

1. /etc/nginx/conf.d/uwsgi.conf

```
server {
    listen       8000;
    server_name  112.74.164.107;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/uwsgi.sock;
    }

    location ~ ^/(404|50x).html$ {
      root  /home/zhengyscn/actual16-opsweb/templates;
      }

    location /static {
        alias /home/zhengyscn/actual16-opsweb/app/static;
    }

    location ~ ^/favicon\.ico$ {
      root  /home/zhengyscn/actual16-opsweb/app/static;
    }
}
```

2. /etc/init.d/uwsgi.ini

```
[uwsgi]
chdir           =  /home/zhengyscn/actual16-opsweb 
home            =  /home/zhengyscn/venv
module          =  manage
callable        =  app 
master          =  true
processes       =  2
socket          =  /tmp/uwsgi.sock
chmod-socket    =  666
logfile-chmod   =  644
daemonize       =  %(chdir)/logs/uwsgi.log
uid             =  uwsgi
gid             =  uwsgi
```

3. start uwsgi

```
uwsgi --ini uwsgi.ini 
```


## 快速生成.gitignore文件

```python
https://www.gitignore.io/
```

## 快速生成requirement.txt的安装文件

```python
pip freeze > requirements.txt
```

## 安装所需要的文件

```python
pip install -r requirement.txt
```


## flask-mail

```python
https://pythonhosted.org/Flask-Mail/

https://github.com/eugene-eeo/mailthon
```


## flask upload file
```
http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
```



```
## return false
http://www.jb51.net/article/40564.htm

## ajax upload file
http://yunzhu.iteye.com/blog/2177923
```
