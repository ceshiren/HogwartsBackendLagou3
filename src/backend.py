from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou3:lagou3@stuq.ceshiren.com:23306/lagou3'
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'seveniruby token'  # Change this!
jwt = JWTManager(app)


# 数据库结构
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# 测试用例表结构定义
class TestCase(db.Model):
    # 可以重新定义表名
    # __tablename__='test_case'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    data = db.Column(db.String(1024), unique=False, nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.name


# 测试用例表结构定义
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String(1024), unique=False, nullable=True)
    testcase_id = db.Column(db.Integer, db.ForeignKey('test_case.id'),
                            nullable=False)
    testcase = db.relationship('TestCase',
                               backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.name


# 用户管理
class Main(Resource):
    def get(self):
        return {'hello': 'world'}


# 用户管理
class UserApi(Resource):
    # 用户查询
    def get(self):
        users = User.query.all()
        return [{'id': u.id, 'name': u.username} for u in users]

    # 用户登录
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            access_token = create_access_token(identity=username)
            return {'msg': 'login success', 'access_token': access_token}
        else:
            return {'msg': 'login fail'}

    # 用户注册
    def put(self):
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return {'msg': 'register success'}

    # 用户账户删除
    def delete(self):
        pass


# 用例管理
class TestCaseApi(Resource):
    @jwt_required
    def get(self):
        return [
            {
                'id': testcase.id,
                'name': testcase.name,
                'data': testcase.data
            } for testcase in TestCase.query.all()
        ]

    @jwt_required
    def post(self):
        """
        /testcase post 表示新增
        /testcase?id=1 post 表示修改
        :return:
        """

        if request.args.get('id'):
            testcase = TestCase.query.filter_by(id=request.args.get('id')).first()
            if request.json.get('name'):
                testcase.name = request.json.get('name')
            if request.json.get('data'):
                testcase.data = request.json.get('data')
            db.session.flush()
            db.session.commit()
        else:
            testcase = TestCase()
            if request.json.get('name'):
                testcase.name = request.json.get('name')
            if request.json.get('data'):
                testcase.data = request.json.get('data')
            db.session.add(testcase)
            db.session.commit()

    @jwt_required
    def put(self):
        pass

    @jwt_required
    def delete(self):
        pass


# 任务管理
class TaskApi(Resource):
    @jwt_required
    def get(self):
        return [
            {
                'id': task.id,
                'log': task.log,
                'testcase_id': task.testcase_id
            } for task in Task.query.all()
        ]

    @jwt_required
    def post(self):
        """
        /task post 表示新增
        :return:
        """
        task = Task()
        if request.json.get('log'):
            task.log = request.json.get('log')
        if request.json.get('testcase_id'):
            task.testcase_id = request.json.get('testcase_id')
        db.session.add(task)
        db.session.commit()


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
