
from flask import Flask, jsonify
from pymongo import MongoClient
import connect
import subprocess

# Initiate Flask api
api = Flask(__name__)


# Routes
@api.route('/')
def ping_server():
    return "Welcome to the world of Mongo!"


@api.route('/animals')
def get_stored_animals():
    '''
    Returns animals in database
    '''
    db=None
    try:
        db = connect.get_db()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in db.animal_tb.find()]
        return jsonify({"animals": animals})
    except Exception as e:
        api.logger.info(e)
        jsonify({'error': "Connection failed"})
    finally:
        if type(db)==MongoClient:
            db.close()


@api.route('/times')
def get_times():
    '''
    Returns system start ups
    '''
    # Copy output.txt from simulator into api
    try:
        with open('/api/output/output.txt', 'r') as f:
            last_login = f.read()
        api.logger.info(f'last_login: {last_login}')
    except Exception as e:
        api.logger.info(e)
        return jsonify({'error': "Connection failed"})

    # Open the file and read its contents
    with open('/api/output_copy.txt', 'a') as f:
        f.write(last_login)

    with open('/api/output_copy.txt', 'r') as f:
        logins = f.read()

    # Return the contents of the file as a JSON response
    return jsonify({'contents': logins})
    

if __name__=='__main__':
    api.run(host="0.0.0.0", port=5000, debug=True)  