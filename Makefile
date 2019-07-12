
.PHONY: db db-clean packages packages-clean test test-clean

packages-clean:
	rm -rf venv/

packages:
	python3 -m venv venv
	. venv/bin/activate; pip install -Ur pip-requirements.txt

db: packages
	python3 manage.py migrate

db-clean:
	dropdb 'axon'
	createdb 'axon'

run: packages
	. venv/bin/activate; python3 manage.py runserver

test: packages
	. venv/bin/activate; python3 manage.py test