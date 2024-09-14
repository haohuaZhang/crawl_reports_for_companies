# py
## mac（已支持）
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


## Windows（待支持）
在 Windows 上，`pyenv` 的原版通常是用于 Unix/Linux 系统的。为了在 Windows 上使用类似的功能，我们可以使用一个名为 `pyenv-win` 的工具，它是 `pyenv` 的一个 Windows 版本。以下是详细步骤，如何安装 `pyenv-win`，然后安装 Python 3.9.6，并安装 `virtualenv`。

### 步骤 1：安装 `pyenv-win`

1. **安装 Git**（如果没有安装）：
   - 首先，你需要安装 Git，因为 `pyenv-win` 通过 Git 安装。
   - 下载并安装 Git：[Git for Windows](https://git-scm.com/download/win)。

2. **通过 Git 安装 `pyenv-win`**：
   - 打开 **PowerShell** 或 **命令提示符** (以管理员身份运行)。

   使用以下命令克隆 `pyenv-win`：

   ```bash
   git clone https://github.com/pyenv-win/pyenv-win.git $HOME\.pyenv
   ```

3. **设置环境变量**：
   - 打开 **系统属性** > **环境变量**。
   - 在用户变量中找到 `Path`，点击**编辑**。
   - 添加以下两行路径（假设你克隆到了默认路径 `%USERPROFILE%\.pyenv`）：
     ```bash
     %USERPROFILE%\.pyenv\pyenv-win\bin
     %USERPROFILE%\.pyenv\pyenv-win\shims
     ```

4. **重启终端**：
   - 完成设置后，关闭并重新打开命令提示符或 PowerShell。

5. **验证安装**：
   - 运行以下命令，确保 `pyenv-win` 已正确安装：
     ```bash
     pyenv --version
     ```

### 步骤 2：使用 `pyenv-win` 安装 Python 3.9.6

1. **列出可用的 Python 版本**：
   - 运行以下命令查看所有可安装的 Python 版本：
     ```bash
     pyenv install --list
     ```

2. **安装 Python 3.9.6**：
   - 运行以下命令安装指定的 Python 版本：
     ```bash
     pyenv install 3.9.6
     ```

3. **设置全局版本**：
   - 安装完成后，你可以将 Python 3.9.6 设置为全局默认版本：
     ```bash
     pyenv global 3.9.6
     ```

4. **验证 Python 安装**：
   - 运行以下命令验证已安装的 Python 版本：
     ```bash
     python --version
     ```

### 步骤 3：安装 `virtualenv`

1. **安装 `virtualenv`**：
   - 运行以下命令来使用 `pip` 安装 `virtualenv`：
     ```bash
     pip install virtualenv
     ```

2. **创建虚拟环境**：
   - 进入你想要创建虚拟环境的项目目录：
     ```bash
     cd path/to/your/project
     ```

   - 使用 `virtualenv` 创建一个新的虚拟环境（例如 `myenv`）：
     ```bash
     virtualenv myenv
     ```

3. **激活虚拟环境**：
   - 在 Windows 上，激活虚拟环境的命令如下：
     ```bash
     myenv\Scripts\activate
     ```

   - 激活成功后，命令提示符前面会显示 `(myenv)`，表示虚拟环境已启用。

4. **安装项目依赖**：
   - 在虚拟环境中，你可以用 `pip` 安装所需的依赖包：
     ```bash
     pip install <package_name>
     ```

5. **退出虚拟环境**：
   - 完成工作后，你可以通过以下命令退出虚拟环境：
     ```bash
     deactivate
     ```

### 总结

通过以上步骤，你在 Windows 上成功安装了 `pyenv-win`，然后使用它安装了 Python 3.9.6，并且安装了 `virtualenv` 来创建和管理 Python 虚拟环境。这使得你可以轻松地在不同的 Python 版本和项目环境之间切换。

 
