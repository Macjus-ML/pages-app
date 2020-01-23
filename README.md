# Pages App was developed while studyng book "Django for beginers"


For detail clone app.


Deploy Heroku.
## 1. Update Pipfile.lock

### Pipfile ###
[requires] python_version = "3.7"

---------------
$ pipenv lock
---------------
## 2. Create Procfile

----------------
$ touch Procfile
----------------
### update Procfile ###
--------------------------------------------
web: gunicorn blog_project.wsgi --log-file -
--------------------------------------------

## 3. Install gunicorn
-------------------------
$ pipenv install gunicorn
-------------------------

## 4. Install whitenoise
-------------------------
$ pipenv install whitenoise
-------------------------

## 5. Update Git
-------------------------------------------------
$ git status
$ git add -A
$ git commit -m "Heroku config files and updates"
$ git push -u origin master
-------------------------------------------------

## 6. Configure Heroku
----------------------------
$ heroku login
$ heroku create news-app-12 (*** change app name if you want)
$ heroku git:remote -a news-app-12
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
