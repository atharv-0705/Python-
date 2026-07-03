
pip install virtualenv            # Install virtualenv package
virtualenv .venv                  # Create a virtual environment named '.venv'    
source .venv/bin/activate         # Linux or MacOS
.\.venv\Scripts\activate          # Windows
pip install -r requirements.txt   # Install packages from requirements file
deactivate


python -m venv .venv             # Alternative way to create virtual environment
.\.venv\Scripts\activate          # Windows
python --version                  # Check Python version in virtual environment
pip list                         # List installed packages in virtual environment
pip install <package_name>       # Install a package in virtual environment
pip list > requirements.txt      # Save installed packages to requirements file
pip install --upgrade pip        # Upgrade pip to the latest version
deactivate                        # Deactivate the virtual environment


