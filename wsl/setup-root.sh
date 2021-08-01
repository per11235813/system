apt update -y
apt upgrade -y 
apt autoremove
apt install -y gcc build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsnappy-dev libreadline-dev libffi-dev curl
apt install -y unixodbc-dev
apt install -y python3-venv python-setuptools python3-dev python3-pip python3-wheel 
apt install -y inxi # system info

curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
apt update -y
ACCEPT_EULA=Y apt install -y msodbcsql17
ACCEPT_EULA=Y apt install -y mssql-tools

# docker cli install
apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

apt update
apt-get install -y docker-ce

# export TZ=Europe/Copenhagen && apt-get install -y tzdata

curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
apt-get install -y nodejs

curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | tee /etc/apt/sources.list.d/yarn.list
apt-get update
apt-get install -y yarn