# SW to install
* keepass
* ditto
* python
* brave
* git
* veracrypt
* wsl
* office
* 7zip
* vscode
* docker
* hyperv
* dotnet sdk


# data og customisering
* log into vscode
* keepass 
    * keeanywhere
    * http connector
* bitlocker keys
* general backup



## Install programs
cd %USERPROFILE%\Downloads
curl https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe --output python-3.8.10-amd64.exe
python-3.8.10-amd64.exe /silent /passive

curl https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe --output python-3.9.7-amd64.exe
python-3.9.7-amd64.exe /silent /passive

curl "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user" --output vs-code-recent.exe

## Git setup and python setup 
cd %USERPROFILE%
mkdir repo
cd repo
git clone https://github.com/per11235813/system.git
git config --global user.email "per11235813@gmail.com"
git config --global user.name "Per Jensen"
setx PATH "%PATH%";%USERPROFILE%\repo\system\psjwin


cd %USERPROFILE%
py -3.9 -m venv venv
.\venv\Scripts\activate.bat
python -m pip install -U pip setuptools wheel
pip install pandas jupyterlab black pydantic fastapi ipython tqdm requests invoke




Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
