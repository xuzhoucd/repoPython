The app is implemented with Django, Ubuntu, deployed on GCP, and tested with Postman. Django and Python are chosen for the test, as Django is a popular web framework that's secure, scalable and easy to use, and Python is productive.

Apart from configuration/deployment, the biggest challenge or tricky part is to parse json with boolean and null values, cause different lauguages treat the values differently, had tried to use djangorestframework and JSONParser, Serializer to do it, it turned out djangorestframework is not supported on GCP, so have to use json.loads as json parser.

There were a couple of tests I was working on during weekend, it took me 1 to 2 days intermittently for the test.
Most code is in nine/views.py, omitted lib/ and env/ dir in the repository which are standard package from https://cloud.google.com/python/django/

# Install glcoud sdk
https://cloud.google.com/sdk/install

# Setup Django on GCP
https://cloud.google.com/python/django/appengine

# Setup Python environment
Run below command after gcloud sdk is installed on your host

cd django

virtualenv env

source env/bin/activate

pip install -r requirements-vendor.txt -t lib/

pip install -r requirements.txt


# Deploy the app to App Engine
gcloud app deploy

https://<your_project_id>.appspot.com
