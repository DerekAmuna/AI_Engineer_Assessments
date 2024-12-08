## terraform

init:
	cd infrastructure && terraform init
	

plan: init
	cd infrastructure && terraform plan

apply: init
	cd infrastructure && terraform apply --auto-approve

destroy: init
	cd infrastructure && terraform destroy --auto-approve

## flask
flask-run:
	export FLASK_APP=app.py
	flask run

## docker

build:
	docker build -t churn-prediction .

docker-run: build
	docker run -it --rm -p 5001:5000 churn-prediction

## zipping

zip:
	@echo "zipping app"
	zip -r churn-app.zip . -x "*.git*" "*.DS_Store" "*.zip" "*.pyc" "__pycache__/*" "*.csv" "*.ipynb"


## aws beanstalk

deploy:
	eb deploy