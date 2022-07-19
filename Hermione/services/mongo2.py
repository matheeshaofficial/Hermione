# Support Dual Mongo DB now
# For free users
from pymongo import MongoClient

from Hermione.conf import get_str_key

MONGO2 = get_str_key("MONGO_URI_2", None)
MONGO = get_str_key("MONGO_DB_URI", required=True)
if MONGO2 == None:
    MONGO2 = MONGO

mongo_client = MongoClient(MONGO2)
db = mongo_client.daisy
