from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd


app = Flask(_name_)
api = Api(app)


class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        json = request.args["name"]
        json = request.args["age"]
        json = request.args["city"]
        req_data = pd.DataFrame({
            'name'      : ['name'],
            'age'       : ['age'],
            'city'      : ['city']
        })
        data = pd.read_csv('users.csv')
        #data = pd.concat([data, req_data], ignore_index=True)
        data = data.append(req_data, ignore_index=True)
        data.to_csv('kullanici.csv', index=False)
        return {'message' : 'Record successfully added.'}, 201

    def delete(self):
        name = request.args['name']
        data = pd.read_csv('users.csv')

        if name in data['name'].values:
            data = data[data['name'] != name]
            data.to_csv('users.csv', index=False)
            return {'message': 'Record successfully deleted.'}, 200
        else:
            return {'message': 'Record not found.'}, 404

class Cities(Resource):
    def get(self):
        data = pd.read_csv('users.csv',usecols=[2])
        data = data.to_dict('records')
        return {'data' : data}, 200

class Name(Resource):
    def get(self,name):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 404


# Add URL endpoints
api.add_resource(Users, '/users')
api.add_resource(Cities, '/cities')
api.add_resource(Name, '/<string:name>')


if _name_ == '_main_':
    # app.run(host="0.0.0.0", port=5000)
    app.run()
