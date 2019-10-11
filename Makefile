PIPENV_FLAGS ?= "--deploy --system"
DJANGO_RUN ?= gunicorn

help:  ## show help
	@grep -E '^[a-zA-Z_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		cut -d':' -f1- | \
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean:  ## clean all temporary files
	find -name '*.pyc' -delete
	find -name '*.pyo' -delete
	find -name '*~' -delete
	find -name '__pycache__' -delete
	find -name '*.mo' -delete

init:  ## install all deps
	pipenv install $(PIPENV_FLAGS)
	pip freeze

firstrussian/static:
	mkdir firstrussian/static

makemessages: firstrussian/static  ## update translation files
	./manage.py makemessages -a -i *.py

compilemessages: firstrussian/static  ## compile translation files
	./manage.py compilemessages

collectstatic: firstrussian/static  ## collect all staticfiles to a single location
	./manage.py collectstatic --no-input

migrate: firstrussian/static  ## run all migrations
	./manage.py migrate

run: firstrussian/static compilemessages collectstatic migrate
	if [ "$(DJANGO_RUN)" = "runserver" ]; \
	then \
		./manage.py runserver_plus 0.0.0.0:8000; \
	else \
		gunicorn --config gunicorn.py firstrussian.wsgi:application; \
	fi
