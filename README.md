# heroku-django
Demonstrates how to run a Django application on Heroku.

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
