# Flask-Submit-Form-Using-MySQL

## Setup

* Install Python3
```
sudo yum install -y python3
```

* Clone App
```
git clone https://github.com/SQLConjuror/Flask-Submit-Form-Using-MySQL.git
```

* cd to the App directory
```
cd Flask-Submit-Form-Using-MySQL
```

* Install and create virtual environment
```
pip3 install virtualenv
python3 -m venv venv
```

* Activate the virtual environment.
```
source venv/bin/activate
```

* Install Flask
```
pip3 install flask
```


* Install required packages
```
pip3 install -r submit_form/requirements.txt
``` 

* Configure your database settings in the "__init__.py" file
```
_config = {
    'user': '<your_db_user',
    'password': '<db_user_password>',
    'host': '<db_host>',
    'database': '<database>',
    'raise_on_warnings': True,
    }
```

* Run App
```
python3 run.py
```


* Open the app in your browser
```
http://localhost:5000/
```
or

```
http://<server_ip>:5000/
```
