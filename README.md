# py
1. 使用python3,目前脚本用的浏览器指定的是mac下火狐浏览器
   
2. 安装启动火狐浏览器的插件
   ```bash
    HOMEBREW_NO_AUTO_UPDATE=1 brew install geckodriver
   ``` 

### 快速开始

安装pyenv，然后开启虚拟环境，命名为myenv.

```bash
HOMEBREW_NO_AUTO_UPDATE=1 brew install pyenv（跳过brew更新慢，直接安装虚拟环境管理插件）
pyenv install 3.9.6 （安装python版本3.9.6）
pyenv install --list
virtualenv myenv  
```


需要改写mac的环境变量,进入环境文件：
   ```bash
    nano ~/.bashrc
   ```

添加下面代码
   ```bash
   export PATH="/Applications/Firefox.app/Contents/MacOS:$PATH"
   export PATH="$PATH:/Users/supplyframe/Library/Python/3.9/bin"

   export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"
   export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
   export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
   ```

刷新环境文件：
   ```bash
    source ~/.bashrc 
   ```
    

进入目录安装依赖:

```bash
pip3 install selenium beautifulsoup4 webdriver-manager urllib3==1.26.16 list
pip install openpyxl pandas lxml

```


编译脚本.

```bash
python3 spider.py
```



 
