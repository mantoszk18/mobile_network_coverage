# mobile_network_coverage

## This is a small project that aims at providing info about 2G/3G/4G network coverage for specifc operators.

### To run the project

* Create a local_settings.py file in the mobile_network_coverage folder
* These local settings should at least hold SECRET_KEY, DEBUG and DATABASE settings tailored to your needs for example:


```python
# this can be retrieved from environment variables
# here it's plaintext in a non-versioned local file
SECRET_KEY = '#gn@rpjy&n%#_dh-1zv**&f)r3)y=jw_gkkezom$-iz5k@eiaru'

DEBUG = True

# for simplicty I will use the sqlite, no need to setup a database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '',
        'PORT': '',
        'NAME': 'network_coverage',
        'USER': 'super_user',
        'PASSWORD': 'secret_password',
    },
    'slow': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
```


* Of course you need to create the database beforehand
* You need to run migrations: `./manage.py migrate`
* Then to load fixtures (operators): `./manage.py loaddata operator_fixture.json`
* Having a CSV with a list of network coverage measures (from French authorities), run the command to load them to the database: `./manage.py import_location_points <path-to-the-filename>`
* The loading might take some time. Can be stopped at any moment for a less complete, but still usable data.
* Run the server and visit for example `http://127.0.0.1:8000/coverage/api/find?q=447+Lieu+Dit+Penfrat+Ploudaniel` for some results
