import json
from typing import List

from flask import app, Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou4:lagou4password@stuq.ceshiren.com:23306/lagou4'

db = SQLAlchemy(app)

# fake db
app.config['db'] = []


@app.route('/')
def hello():
    return 'hello from ceshiren.com'


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<TestCase %r>' % self.username


class TestCaseService(Resource):
    def get(self):
        """
        测试用例的浏览获取 /testcase.json /testcase.json?id=1
        """
        testcases: List[TestCase] = TestCase.query.all()
        res = [{
            'id': testcase.id,
            'name': testcase.name,
            'description': testcase.description,
            'steps': json.loads(testcase.steps)
        } for testcase in testcases]
        return {
            'body': res
        }

    def post(self):
        """
        上传用例， 更新用例
        /testcase.json  {'name': 'xx', 'description': 'xxx', 'steps': []}
        """
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('description'),
            steps=json.dumps(request.json.get('steps'))
        )
        db.session.add(testcase)
        db.session.commit()
        return 'ok'


#todo: 作业1
# 完成TaskService的功能，基本的增删改查
# 拔高：增加的时候关联TestCase
class TaskService(Resource):
    def get(self):
        pass


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
