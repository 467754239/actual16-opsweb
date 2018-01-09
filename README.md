# OpsWeb Platform(beta)

[demo](http://www.vksrc.com:8000)

```
赞赏！！！Start....
```


## 工作(代理)模式 
nginx + uwsgi + flask + virtualenv


## 配置
1. /etc/nginx/conf.d/uwsgi.conf

```bash
server {
    listen       80:;
    server_name  localhost;

    location / {
        include uwsgi_params;

        # 替换本地uwsgi unix sock文件路径
        uwsgi_pass unix:/tmp/uwsgi.sock;
    }

    location ~ ^/(404|50x).html$ {
        # flaskHTML文件路径
        root  /home/zhengyscn/actual16-opsweb/templates;
    }

    location /static {
        # flask静态JS/CSS/IMG等文件路径
        alias /home/zhengyscn/actual16-opsweb/app/static;
    }

    location ~ ^/favicon\.ico$ {
        # flask静态JS/CSS/IMG等文件路径
        root  /home/zhengyscn/actual16-opsweb/app/static;
    }
}
```

2. /etc/init.d/uwsgi.ini

```bash
[uwsgi]
chdir           =  /home/zhengyscn/actual16-opsweb   # flask项目目录路径
home            =  /home/zhengyscn/venv              # env虚拟目录路径
module          =  manage
callable        =  app 
master          =  true
processes       =  2
socket          =  /tmp/uwsgi.sock                   # unix sock文件路径
chmod-socket    =  666
logfile-chmod   =  644
daemonize       =  %(chdir)/logs/uwsgi.log
uid             =  uwsgi
gid             =  uwsgi
```

3. start uwsgi

```bash
$ cd bin
$ sh start.sh
```

4. 安装所需要的文件

```python
pip install -r requirement.txt
```

## 参考
```
# flask upload file
http://flask.pocoo.org/docs/0.10/patterns/fileuploads/

## return false
http://www.jb51.net/article/40564.htm

## ajax upload file
http://yunzhu.iteye.com/blog/2177923
```
