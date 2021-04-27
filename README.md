# heroku-django
Demonstrates how to run a Django application on Heroku.

## Create Heroku Application
Before you can create a heroku application you need to login.

    heroku login

To create the heroku application you use the following command.

    heroku create <application name>

This application was created using the following command.

    heroku create heroku-django-application

The app has the following url.

    https://heroku-django-application.herokuapp.com/

The following is the heroku git repo for the app.

    https://git.heroku.com/heroku-django-application.git

## Allowed hosts
You will need to add heroku-django-application.herokuapp.com to the
ALLOWED_HOSTS in the settings. At the same time you probably want to
add 0.0.0.0 and localhost.

## Deploying to Heroku with Git
Heroku applications are deployed with git. If you created your
application with the command `heroku create` then the heroku remote
will have already been created for you.

    $ git remote -v
    heroku	https://git.heroku.com/heroku-django-application.git (fetch)
    heroku	https://git.heroku.com/heroku-django-application.git (push)
    origin	git@gitlab.com:treadup/heroku-django.git (fetch)
    origin	git@gitlab.com:treadup/heroku-django.git (push)

Otherwise you will have to create it yourself.

To deploy to heroku use the following command.

    git deploy heroku master

## Static assets
Django does not support serving static assets in production. There is
a third party package called whitenoise that can be used for this.
The whitenoise project allows you to serve static assets from a Django
application in production. Using whitenoise can be a good practice
even if you are not deploying to Heroku.

To install whitenoise just use the following command.

    pip install whitenoise

Then add the following middleware just after the security middleware.

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        ...
    ]

See the following links for more information about whitenoise.
https://devcenter.heroku.com/articles/django-assets#whitenoise
http://whitenoise.evans.io/en/stable/

## Specifying Python Runtime
You can tell Heroku which version of Python to use when running your
code by adding a runtime.txt file. The contents of a runtime.txt file
looks something like the following.

    python-3.9.4

See the following link for more information about specifying the
Python runtime.
https://devcenter.heroku.com/articles/python-runtimes

## Gunicorn WSGI server
Django has a built in webserver but this webserver should not be used
in production. Instead we need to use a third party webserver. The
server that I usually go with is Gunicorn.

    pip install gunicorn

## Procfile
The Procfile is used to tell heroku what processes to run. You can run
both a web process and background processes.

The Procfile has the filename Procfile and should be located in the
root of the git repo. It has the following format.

    <process type>: <command>

For web applications the process type is web.

    web: <command>

To run a Django application with gunicorn you would use the following
command.

    web: gunicorn <django project name>.wsgi

In our case the Django project is called herokudjango. That means our
Procfile should look like the following.

    web: gunicorn herokudjango.wsgi

https://devcenter.heroku.com/articles/procfile

## Postgres
To install the database client for Postgres use the following command.

    pip install psycopg2-binary

Next you need to configure the database settings in the settings.py
file.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'databasename',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'hostname',
            'PORT': '5432'
        }
    }

## Heroku Postgres
To provision a postgres server for your heroku application use the
following command.

    heroku addons:create heroku-postgresql:hobby-dev

See the following link for more information about Heroku Postgres.
https://elements.heroku.com/addons/heroku-postgresql

## Heroku Postgres connection string
Heroku will provide a connection string to your application as an
environment variable. This connection string has the following format.

    postgres://USER:PASSWORD@HOST:PORT/NAME

To see your current connection string you can use the following command.

    heroku config:get DATABASE_URL -a your-app

## dj_database_url
The dj_database_url package can read a Heroku connection string and
return the data in a format suitable for a django application. First
install it using the following command.

    pip install dj-database-url

Then configure the database connection using dj_database_url in the
settings.py file.

    import dj_database_url
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

See the following urls for more information.
https://github.com/kennethreitz/dj-database-url
https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python

## Running Django migrations on Heroku
When deploying the application to Heroku you want to run the database
migrations as part of the deployment step. Do this by adding the
following command as the first line in the Procfile

    release: python manage.py migrate

See the following url for more information.
https://help.heroku.com/GDQ74SU2/django-migrations

## Create remote superuser
To create a super user on the remote system use the following command.

    heroku run python manage.py createsuperuser

## Media files in S3
To have the media files stored in S3 you have to configure a storage
engine that can work with S3. We are going to be using
django-storages. Since we are working with AWS we will also need to
install boto3.

    pip install boto3 django-storages

Next we configure Django to use the S3Boto3Storage engine when working
with media files.

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

You have to set the following environment variables.

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME

See the following URL for more information.
https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

## Heroku Headers
Heroku adds the following headers to your requests.

- X-Forwarded-For: the originating IP address of the client connecting to the Heroku router
- X-Forwarded-Proto: the originating protocol of the HTTP request (example: https)
- X-Forwarded-Port: the originating port of the HTTP request (example: 443)
- X-Request-Start: unix timestamp (milliseconds) when the request was received by the router
- X-Request-Id: the Heroku HTTP Request ID
- Via: a code name for the Heroku router

To see if the original request is using http or https look at the
X-Forwareded-Proto header.

See the following URL for more information.
https://devcenter.heroku.com/articles/http-routing#heroku-headers

## Force TLS
Heroku
To force the Django application to use TLS/SSL you can use the
following middleware.

    MIDDLEWARE = [
        # SecurityMiddleware must be listed before other middleware
        'django.middleware.security.SecurityMiddleware',
        # ...
    ]

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

See the following URL for more information.
https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
