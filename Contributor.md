Simple Restful Api With Python and Flask 
=========================================

To start working

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone https://github.com/Emmanuel-Nika-CompSci/Maintenance-Tracker-App-Flask-API.git
    $ git install flask

Or you could use::

    $ pip install python-flask


Run
---

::

    $ export FLASK_APP=app
    $ export FLASK_ENV=development
    $ flask init-db
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=app
    > set FLASK_ENV=development
    > flask init-db
    > flask run

OR: 

    $ export FLASK_APP=app
    $ export FLASK_ENV=development
    $ python app.py

Or on Windows cmd::

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > python app.py run

Open http://127.0.0.1:5000 in a browser.
