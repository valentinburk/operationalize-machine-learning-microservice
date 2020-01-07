setup:
	python -m venv .devops
	. .devops/Scripts/activate

install:
	python -m \
	pip install --upgrade pip && \
	pip install -r requirements.txt

lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1202,W1203 app.py

all: install lint test
