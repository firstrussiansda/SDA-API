PIPENV_FLAGS ?= "--deploy --system"
RUN_CMD ?= runserver

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

install:  ## install all deps
	pipenv install $(PIPENV_FLAGS)
	pip freeze

makemessages:  ## update translation files
	./manage.py makemessages -a -i *.py

compilemessages:  ## compile translation files
	./manage.py compilemessages

collectstatic:  ## collect all staticfiles to a single location
	./manage.py collectstatic --no-input

migrate:  ## run all migrations
	./manage.py migrate

run: compilemessages collectstatic migrate
	./manage.py $(RUN_CMD) 0.0.0.0:8000
