from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


#用户管理
class Main(Resource):
    def get(self):
        return {'hello': 'world'}


#用户管理
class UserApi(Resource):
    def get(self):
        return {'hello': 'world'}

#用例管理
class TestCaseApi(Resource):
    def get(self):
        return {'hello': 'world'}

#任务管理
class TaskApi(Resource):
    def get(self):
        return {'hello': 'world'}

#报告管理
class ReportApi(Resource):
    def get(self):
        return {'hello': 'world'}



api.add_resource(Main, '/')
api.add_resource(UserApi, '/login')
api.add_resource(TestCaseApi, '/testcase')
api.add_resource(TaskApi, '/task')
api.add_resource(ReportApi, '/report')

if __name__ == '__main__':
    app.run(debug=True)

