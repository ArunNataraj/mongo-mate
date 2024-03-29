"""List Of Constants"""
EXP = "exp"
EXP_MINS = 30
AUTHORIZATION = "authorization"
SPACE = " "
INVALID_EXPIRED_TOKEN = "Invalid or expired token"
ACCESS_TOKEN_MISSING = "Access Token Missing"
MONGO_ID = "_id"
MONGO_SET = "$set"
STARTUP = "startup"
CRUD = "crud"
SESSION = "session"
ALL_ORIGIN = "*"
COLLECTION_NAMES = "collection_names"
MESSAGE = "message"
RECORDS = "records"
USER = "user"
EMAIL = "email"
INSERT_ONE = "insert_one"
INSERT_MANY = "insert_many"
FIND_ONE = "find_one"
FIND_MANY = "find_many"
DELETE_ONE = "delete_one"
DELETE_MANY = "delete_many"
UPDATE_ONE = "update_one"
UPDATE_MANY = "update_many"
QUERIES = "queries"
FIELD = "field"
OPERATOR = "operator"
EQUALS = "equals"
VALUE = "value"
USER_REGISTRATION_MSG = "User Registered in Successfully"
QUERY_EXC_MSG = "Query Executed Successfully"
QUERY_RETRIEVED_MSG = "Pre Defined Queries Retrieved Successfully"
RECORD_DELETED_MSG = "Record(s) Deleted From The Collection Successfully"
RECORD_UPDATED_MSG = "Record(s) Updated To The Collection Successfully"
RECORD_INSERTED_MSG = "Record(s) Inserted To The Collection Successfully"
RECORD_RETRIEVE_MSG = "Record(s) Retrieved From The Collection Successfully"
COLLECTION_MSG = "Collection Names Retrieved From The Data Base Successfully"
ACCESS_TOKEN = "access_token"
USER_LOGIN_MSG = "User Logged in Successfully"
USER_LOGOUT_MSG = "User Logged Out Successfully"
INVALID_PASS = "Invalid Password"
NOT_REGISTERED = "User Not Registered / Invalid Email"
QUERY1 = "query1"
QUERY2 = "query2"
QUERY3 = "query3"
QUERY4 = "query4"
QUERY5 = "query5"
QUERY6 = "query6"
PRE_DEFINED_QUERIES = {
    "query1": {"Create The Collection": "collection_name"},
    "query2": {"Index The Collection": "field_name"},
    "query3": {"Sort The Collection in Ascending Order": "field_name"},
    "query4": {"Sort The Collection in Descending Order": "field_name"},
    "query5": {"View the Limited Number Of Records": "limit_count"},
    "query6": {"Fetch Only Particular Columns From The Collection": "field_names"}
}
