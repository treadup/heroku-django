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
