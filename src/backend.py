from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou3:lagou3@stuq.ceshiren.com:23306/lagou3'
db = SQLAlchemy(app)


# 数据库结构
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# 用户管理
class Main(Resource):
    def get(self):
        return {'hello': 'world'}


# 用户管理
class UserApi(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'name': u.username} for u in users]


# 用例管理
class TestCaseApi(Resource):
    def get(self):
        return {'hello': 'world'}


# 任务管理
class TaskApi(Resource):
    def get(self):
        return {'hello': 'world'}


# 报告管理
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
