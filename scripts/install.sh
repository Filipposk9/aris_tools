echo "Creating a virtual environment..."
python3 -m venv env

echo "Activating the virtual environment..."
source env/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing required packages..."
pip install -r requirements.txt

echo "Installation complete!"