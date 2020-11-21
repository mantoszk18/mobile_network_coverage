# mobile_network_coverage

## This is a small project that aims at providing info about 2G/3G/4G network coverage for specifc operators.

### To run the project
* You need to run migrations: `./manage.py migrate`
* Then to load fixtures (operators): `./manage.py loaddata operator_fixture.json`
* Having a CSV with a list of network coverage measures (from French authorities), run the command to load them to the database: `./manage.py import_location_points <path-to-the-filename>`
* The loading might take some time. Can be stopped at any moment for a less complete, but still usable data.
* Run the server and visit for example `http://127.0.0.1:8000/coverage/api/find?q=447+Lieu+Dit+Penfrat+Ploudaniel` for some results
