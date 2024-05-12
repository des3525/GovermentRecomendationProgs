from flask import Flask, request
from model import ModelClass
import json
app = Flask(__name__)
model = ModelClass()

@app.route('/condition', methods=['GET'])
def getCondition():
	file = request.args.get('filename')
	return str(model.query(file))

@app.route('/reload-index', methods=['GET'])
def reloadIndexs():
	model.loadToStore()
	return

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8056)