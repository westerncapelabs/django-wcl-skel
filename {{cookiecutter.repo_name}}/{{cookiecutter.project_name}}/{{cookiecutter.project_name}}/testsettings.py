from {{cookiecutter.project_name}}.settings import *  # flake8: noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TESTSEKRET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

# LOCAL
SERVICES_ENDPOINT_PRODUCTS = "http://core-products.local:8001/products"
SERVICES_ENDPOINT_SUBSCRIPTIONS = "http://core-subscriptions.local:8003/subscriptions"
SERVICES_ENDPOINT_CUSTOMERS = "http://core-customers.local:8002/customers"
SERVICES_ENDPOINT_ORDERS = "http://core-orders.local:8004/orders"
SERVICES_ENDPOINT_ANALYTICS = "http://core-analytics.local:8005/analytics"

SERVICES_TOKEN_PRODUCTS = "df064ea03fe60fdfb2650c05639e2637e122c042"
SERVICES_TOKEN_SUBSCRIPTIONS = "8efb6262c2ad534fbe3241405813e86f7ac78554"
SERVICES_TOKEN_CUSTOMERS = "e2ea448055431bb0be7018731bf9983c5d7d6bcf"
SERVICES_TOKEN_ORDERS = "74fba118f4e4672636c639d9ecbf30dfbd31cc00"
SERVICES_TOKEN_ANALYTICS = "8ab00c2bf683a2ffedcebd3c1168fa09bc41aed4"

MANDRILL_TOKEN = "D34GBN7_tEEYGaIW3me4QQ" # test
