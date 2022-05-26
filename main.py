from pymongo import MongoClient
import certifi
# The string is a cluster


cluster = MongoClient("mongodb+srv://admin:<pass>@cluster0.lgtos.mongodb.net/test?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = cluster['test']
collection = db['test']

