
##一、系统环境

###tornado版本：4.5.1
###Django版本：2.0
###nginx版本：1.12.2
###python版本：3.6.1
###MySQL版本：5.7
<br>
##二、使用步骤
###1、下载git项目到本地
###2、需要安装上面所说的软件，请确保MySQL的端口为3306，如果MySQL的端口不是3306请修改MySQL的端口，或者将helloword-->hellword目录中的settings.py中的3306修改为你本机所设置的MySQL端口。
###3、修改nginx-1.12.2-->conf-->nginx.conf中的root（75行和102行）所指向项目的APP目录，修改为你下载项目的APP目录
###4、在MySQL中建立一个test的数据库，如果没有执行下面的命令的时候可能会报错。
###5、打开cmd进入到helloword-->helloword中，与manage.py位于同一目录下，输入以下命令，在MySQL中生成user表。
###python manage.py makemigrations  
###python manage.py migrate  
###6、打开MySQL workbench，找到test数据库找到里面的user表，设置用户名和密码
###7、点击nginx.exe启动，运行server.py
###8、输入127.0.0.1即可看到PID的界面，多次刷新可以看到不同的PID
###9、输入127.0.0.1/login/进行登录
<br>
##三、可能会遇到的问题
###1、运行第五步中的命令时，如果报Did you install mysqlclient?输入以下命令即可解决
###pip install mysqlclient 
###2、如果在运行server.py的过程中报no module MySQLdb
###解决办法：MySQLdb不支持python3.6，我们可以安装pymysql，并在settings.py中添加以下代码，添加在installed_apps之前
###try:
###    import pymysql
###    pymysql.install_as_MySQLdb()
###except ImportError:
###    pass
###3、在启动nginx的时候，需要注意是否启动成功，可以在logs目录中的error.log中查看错误日志输出，如果没有输出表示启动成功，在任务管理器-->进程中可以看到nginx的相关进程
###4、如果点击登录的时候没有反应，在控制台中输出了CSRF cookie not set django…verification failed
###请确保settings.py中的'django.middleware.csrf.CsrfViewMiddleware',已经被注释







