请察看服务器上的日志文件/var/log/secure, 这里有很多有用的信息

非常重要的一点是，.ssh目录必须是700权限，而authorized_keys必须只有用户拥有写权限，否则ssh服务器会拒绝用户登陆。

参考资料:
* [linux ssh 使用深度解析（key登录详解）](http://blog.lizhigang.net/archives/249)
