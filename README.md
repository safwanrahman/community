Community Dashboard
=====

Its a Django app build for Mozillians Community Dashboard. It would fetch data from Mozillians API and show country wise informations.
For more information, see [participation-org/issues/133](https://github.com/mozilla/participation-org/issues/133).
# Set Up

For importing data from Mozillians API, you need a API Key. For inormations about getting API Key, check [Mozillians API V2 Documentaion](http://mozillians.readthedocs.org/en/latest/api/apiv2)

For Developing purposes, please set up the app with **Development Setup**. Otherwise it will need a lot of time to fetch the data from the Mozillians API.

### Setting up for Normal use
* Install [pip](http://www.pip-installer.org/en/latest/)
* Install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
* Create a Virtual Environment: ``virtualenv ven``
* Now activate the virtualenv: ``source venv/bin/activate``
* Install python dependencies: ``pip install django==1.8.4 requests==2.7.0``
* There is a file called ``settings_locale.py.dist`` under ``./mozillians`` directory. Change the file name from ``settings_local.py.dist`` to ``settings_local.py``
* **Add API Keys into ``API_KEY`` field of ``settings.py``**
* Create a database by running ``./manage.py migrate``
* You will a get a file ``config.py`` in ``/dashboard`` directory. By default top 10 countries are added into there and will fetch data for that 10 Countries only. So if you want to fetch any other country's data, please add another entry into the ``COUNTRIES`` field. You are free to remove any country from there to get only your desired country's data. But be informed that gathering lower number of country's data **will not** affect much time of the set up. Because all the skills data are needed to be fetched.
* Then to get data from Mozillians API:
 * Run ``./manage.py fetchdata`` to get the user data
 * Then run ``./manage.py fetchskills`` to get all the skill data
   * **Please Be patience, it will take a long long time depeneds on your connection and system**
* **Then run ``./manage.py runserver`` to start the app**
* Then check ``127.0.0.1:8000/result`` for getting the dashboard

### Setting up for Development
**If you dont have time to run all the things for development, Some Public data is already gathered**. You can load the public data easily by following the instructions.
* Install python dependencies: ``pip install django==1.8.4 requests==2.7.0``
* There is a file called ``settings_locale.py.dist`` under ``/mozillians`` directory. Change the file name from  ``settings_local.py.dist`` to ``settings_local.py``
* Create a database by running ``./manage.py migrate``
* Load the data by running ``./manage.py loaddata data``
* Run ``./manage.py runserver`` to start the application
* **Then check ``127.0.0.1:8000/result`` for getting the dashboard**
