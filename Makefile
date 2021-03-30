serve:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

check:
	python3 manage.py check

test:
	python3 manage.py test