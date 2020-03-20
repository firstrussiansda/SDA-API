PIPENV_FLAGS ?= "--deploy --system"
DJANGO_RUN ?= gunicorn
DJANGO_STATIC_ROOT?=firstrussian/static
DJANGO_MEDIA_ROOT?=firstrussian/media

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

dumpdata:  ## dump test data fixtures
	./manage.py dumpdata \
		--all \
		--exclude=admin \
		--exclude=sessions \
		--exclude=contenttypes \
		--indent=2 \
		> fixtures.json

loaddata:  ## load test data fixtures
	./manage.py loaddata fixtures.json

lint:
	pre-commit run --all-files

$(DJANGO_STATIC_ROOT):
	mkdir $(DJANGO_STATIC_ROOT)

$(DJANGO_MEDIA_ROOT):
	mkdir $(DJANGO_MEDIA_ROOT)

makemessages: $(DJANGO_STATIC_ROOT)  ## update translation files
	./manage.py makemessages -l ru --no-location
	./manage.py makemessages -l uk --no-location

compilemessages: $(DJANGO_STATIC_ROOT)  ## compile translation files
	./manage.py compilemessages

collectstatic: $(DJANGO_STATIC_ROOT)  ## collect all staticfiles to a single location
	./manage.py collectstatic --no-input

migrate: $(DJANGO_STATIC_ROOT)  ## run all migrations
	./manage.py migrate

run: $(DJANGO_STATIC_ROOT) $(DJANGO_MEDIA_ROOT) compilemessages collectstatic migrate
	if [ "$(DJANGO_RUN)" = "runserver" ]; \
	then \
		./manage.py runserver_plus 0.0.0.0:8000; \
	else \
		gunicorn --config gunicorn.py firstrussian.wsgi:application; \
	fi
