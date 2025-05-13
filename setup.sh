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
