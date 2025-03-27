# v2register
v2机场炸库注册机
✅ 多线程并发：使用 threading，同时跑 10-10000（自定义） 个线程，加快注册速度。看你配置和目标站点配置调整
✅ 优化浏览器实例：每个线程一个 Chrome 实例，减少资源占用。
✅ 随机时间间隔：time.sleep(random.uniform(2, 5)) 避免触发风控。
✅ 日志输出更清晰：可以直观看到哪个线程在注册哪些账号。


脚本1的安装环境：


如果 Chrome 没有安装，请执行以下命令安装 Chrome（适用于 Ubuntu/Debian）：
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

sudo apt-get install -f


如果使用的是 CentOS，可以运行：

sudo yum install -y google-chrome-stable

网站检测 Selenium，使用 undetected_chromedriver 规避
运行：pip install undetected-chromedriver


运行：pip install selenium webdriver-manager

修改zc.py里的https://xxxxx/#/register   改完你要注册的机场地址

默认每个线程注册50个号，10个线程

for i in range(50)# -这里的50是50个号，自行修改

num_threads = 10  # 10个线程，每个线程注册50个账号


开始运行注册脚本：python3/python zc.py


账号密码保存在accounts.txt文件

格式：
aBc123xyz@gmail.com | P4ssW0rDxyz!
m9Kq8ZrXq@163.com | Asdf1234QWER

建议：screen 后台运行


脚本2教程
✅ 使用 requests 直接调用 API：比 selenium 方式快 100 倍。
✅ 使用 threading 并发：10 个线程同时注册，提高效率。
✅ random.uniform(1, 3) 延迟：防止 API 风控。
✅ 自动保存注册成功的账号：写入 accounts.txt，方便管理。


这样 10 -10000个线程（自行定义） 并发，每个线程 50 个账号（自行定义），一次性可以注册 百万个账号，效率大大提升！


修改zc.py里的https://xxxxx/api/v1/passport/auth/register   改完你要注册的机场的API地址 如果前后端分离的请自行抓包

默认每个线程注册500000个号，50个线程
for i in range(50)# -这里的500000是500000个号，自行修改

num_threads = 50  # 50个线程，每个线程注册500000个账号

运行：python3/python zcapi.py


ps：本脚本仅支持未开验证的机场，开了验证的请自行优化! 下个版本加刷邮箱。
