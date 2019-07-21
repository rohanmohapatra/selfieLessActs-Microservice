#selfielessacts/__init__.py
from app import app
from db_setup import init_db
from flask_cors import CORS
from views.users import users
from views.miscs import miscs
from views._count import _count
from views._count import requestCounter
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--port")
args = parser.parse_args()
port = int(args.port)

base_url = '/api/v1'

#init_db()

app.register_blueprint(users, url_prefix=base_url+'/users')
app.register_blueprint(miscs, url_prefix=base_url+'/miscs')
app.register_blueprint(_count, url_prefix=base_url+'/_count')

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.',500

@app.errorhandler(405)
def method_not_allowed(e):
	requestCounter[0] +=1
    # note that we set the 405 status explicitly
	return 'Method Not Allowed',405

if __name__=="__main__":
	#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
	app.run(host='0.0.0.0', port=port,debug=True)
	
