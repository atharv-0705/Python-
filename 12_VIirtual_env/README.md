
## Install virtualenv package
pip install virtualenv            

## Create a virtual environment named '.venv'
virtualenv .venv                  

## Linux or MacOS
source .venv/bin/activate         

## Windows
.\.venv\Scripts\activate          

## Install packages from requirements file
pip install -r requirements.txt   
deactivate


# Alternative way to create virtual environment
python -m venv .venv             

## Windows
.\.venv\Scripts\activate          

## Check Python version in virtual environment
python --version                  

## List installed packages in virtual environment
pip list                         

## Install a package in virtual environment
pip install <package_name>       

## Save installed packages to requirements file
pip list > requirements.txt      

## Upgrade pip to the latest version
pip install --upgrade pip        

## Deactivate the virtual environment
deactivate                        


