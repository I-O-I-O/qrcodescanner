mkdir qrscanner
python3 -m venv qrscanner
cd qrscanner
bin/pip install pyzbar
bin/pip install opencv-python opencv-contrib-python
bin/pip install selenium
wget https://raw.githubusercontent.com/I-O-I-O/qrcodescanner/refs/heads/main/scanner.py
