# Bank app documentation

Build requirements.txt after package update : `python3 -m  pipreqs.pipreqs . --force` or `pip install -r requirements.txt`

Create .env file at the root. Example content :

DATABASE_USERNAME="melo"
DATABASE_PASSWORD="/Xcsdsvbpa137$"
DATABASE_HOST="192.168.1.10"
DATABASE_PORT=3306
DATABASE_TABLE="banque"
DATABASE_CERT_FILE="ca-certificate.crt"

Run app GUI with `python3 main.py` of CLI with `python3 distributeur.py`