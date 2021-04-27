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

## Create remote superuser
To create a super user on the remote system use the following command.

    heroku run python manage.py createsuperuser
