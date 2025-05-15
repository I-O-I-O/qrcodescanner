echo "Creating folder..."
mkdir qrscanner

echo "Creating environment..."
python3 -m venv qrscanner
cd qrscanner

echo "Installing pyzbar..."
bin/pip install pyzbar

echo "Installing opencv-python & opencv-contrib-python..."
bin/pip install opencv-python opencv-contrib-python

echo "Installing selenium..."
bin/pip install selenium

echo "Fetching scanner.py"
wget https://raw.githubusercontent.com/I-O-I-O/qrcodescanner/refs/heads/main/scanner.py

cd 

echo "Updating apt"
sudo apt update

echo "Installing firefox-esr"
sudo apt install firefox-esr

echo "Fetching geckodriver"
wget https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux-aarch64.tar.gz

tar -xvzf geckodriver-v0.36.0-linux-aarch64.tar.gz

chmod +x geckodriver

sudo mv geckodriver /usr/local/bin/

