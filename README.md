<!---------------------------------------[Description]-->
## Description
    This is a example of python with fastapi for API



<!---------------------------------------[Install]-->
<br><br><br>

## Source 
    git clone git@github.com:kashanimorteza/example_python_fastapi.git
    cd ./example_python_fastapi



<!---------------------------------------[Python]-->
<br><br><br>

## Python

#### Install
    add-apt-repository ppa:deadsnakes/ppa
	apt update -y
	apt install python3 -y
	apt install python3-pip -y
	apt install python3-venv -y

#### Virtual environment 
	python3 -m venv .myenv3
	.myenv3/bin/python3 -m pip install --upgrade pip
	source .myenv3/bin/activate
	pip install -r requirements.txt



<!---------------------------------------[WebApi]-->
<br><br><br>

## WebApi

#### Create SSL
    openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -nodes

#### Run simple
	fastapi run ./api.py

#### Run HTTP
    uvicorn api:app --host 0.0.0.0 --port 8000

#### Run HTTPS
    uvicorn webapi.api:app --host 0.0.0.0 --port 8000 --ssl-keyfile=webapi/key.pem --ssl-certfile=webapi/cert.pem

#### Chrome
	http://0.0.0.0:8000

#### Doc
	http://0.0.0.0:8000/docs

<!---------------------------------------[Structure]-->
<br><br><br>

## Structure

	Api
	Route
	Logic
	Lib
	Model