python3 -m venv ~/venv
. ~/venv/bin/activate

python -m pip install -U pip setuptools wheel
pip install jupyter invoke pydantic pandas black

echo ". ~/venv/bin/activate"  >> ~/.bashrc
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc


