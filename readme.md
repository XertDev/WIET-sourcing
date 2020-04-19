# WIET-sourcing
![Deploy to Heroku](https://github.com/XertDev/WIET-sourcing/workflows/Deploy%20to%20Heroku/badge.svg?branch=master)
## Development setup
### Basic setup 
You can clone the app source and create venv with all requirements installed by running the code below. 
```shell script
git clone https://github.com/XertDev/WIET-sourcing.git
cd WIET-sourcing
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
Then everytime you need, you can access the venv created by running the command below. 
```shell script
source venv/bin/activate
```
### Instance configuration
This app need "SQLALCHEMY_DATABASE_URI" variable configured. 

You can create "instance/config.py" file for local run configuration. If that is a case for you, please follow the syntax below.  
```python
SQLALCHEMY_DATABASE_URI='here_past_your_uri'
``` 
Alternatively, you can also create local variable by shell export. 
### Running via shell
For the development setup it is recommended to use "FLASK_ENV" variable. You can create it by running the command below.
```shell script
export FLASK_ENV=development
``` 
To make "flask run" command run these configuration, you need to add local variable "FLASK_APP" pointing to "WIET_sourcing/\_\_init__.py", by running.
```shell script
export FLASK_APP=WIET_sourcing/__init__.py
``` 
To remove any local variable you can use.
```shell script
unset VARIABLE_NAME
```
### Running from pycharm
You can specify venv for pycharm to use by
 
 File -> Setting -> Project -> Python interpreter -> gear icon -> Add -> Existing -> set interpreter path to point to your "venv/bin/python" file -> Ok  
 
 Then you can create "flask server" run configuration specifying "Module name" as "WIET_sourcing", "FLASK_ENV" as "development", and using "Python interpreter" pointed before. 
 
 ![Configuration example](https://media.discordapp.net/attachments/700042930760581195/700262052047880212/unknown.png?width=720&height=611)
 
 ## Heroku deployment
 The app is deployed under [this](https://wiet-sourcing.herokuapp.com/) address by github action after every push on master branch. 
 
 The heroku authorization is set as secret in github repository settings.
 
 On heroku the app runs under gunicorn wsgi server. The heroku formation is configured by "Procfile". It points to "wsgi.py" script, by which the app is started (note that it is **not** the same configuration as the local one provided in previous sections of this document). 
 
 The heroku app provides "FLASK_ENV=production" and "SQLALCHEMY_DATABASE_URI" enviroment variables. Those can be managed by commands listed below. 
 ```shell script
# list all variables
heroku config 
# create variable
heroku config:set VARIABLE_NAME=variable_value
# remove variable 
heroku config:unset VARIABLE_NAME
```
