import json
import os
from typing import List

from flask import app, Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# mysql
app.config['SQLALCHEMY_DATABASE_URI']: Jenkins = 'mysql+pymysql://lagou4:lagou4password@stuq.ceshiren.com:23306/lagou4'

app.config['jenkins'] = Jenkins(
    'http://stuq.ceshiren.com:8020/',
    username='seveniruby',
    password='11fbcfb9793b526ef147258c968ce62543'
)

db = SQLAlchemy(app)

# fake db
app.config['db'] = []


@app.route('/')
def hello():
    return 'hello from ceshiren.com'


class TestCase(db.Model):
    __tablename__ = 'lagou4_seveniruby_testcase'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)

    # task_id = db.Column(db.Integer, db.ForeignKey('lagou4_seveniruby_task.id'),
    #                     nullable=False)
    # task = db.relationship('Task',
    #                        backref=db.backref('testcases', lazy=True))

    def __repr__(self):
        return '<TestCase %r>' % self.username


class Task(db.Model):
    __tablename__ = 'lagou4_seveniruby_task'
    id = db.Column(db.Integer, primary_key=True)
    testcases = db.Column(db.String(1024), nullable=True)

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


# todo: 作业1
# 完成TaskService的功能，基本的增删改查
# 拔高：增加的时候关联TestCase
class TaskService(Resource):
    def get(self):
        id = request.args.get('id')
        if id:
            task = Task.query.filter_by(id=id).first()
            # os.system('pytest xx') use jenkins replace
            return {
                'msg': 'ok',
                'body': json.loads(task.testcases)
            }
        else:
            tasks = Task.query.all()
            return {
                'msg': 'ok',
                'body': [json.loads(task.testcases) for task in tasks]
            }

    def post(self):
        """
        上传用例， 更新用例
        /task.json  {'testcases': [1,2,3,4]}
        """

        testcases_id = request.json.get('testcases')
        task = Task(testcases=json.dumps(testcases_id))
        db.session.add(task)
        db.session.commit()
        return {
            'msg': 'ok'
        }

    def put(self):
        id = request.json.get('id')
        if id:
            task = Task.query.filter_by(id=id).first()
            testcases_info=[]
            for id in json.loads(task.testcases):
                testcase = TestCase.query.filter_by(id=int(id)).first()
                case_info = {
                    'name': testcase.name,
                    'steps': testcase.steps
                }
                testcases_info.append(case_info)

            task_info = {
                'id': task.id,
                'testcases': testcases_info
            }
            # os.system('pytest xx') use jenkins replace
            jenkins: Jenkins = app.config['jenkins']
            jenkins['lagou4_testcase'].invoke(
                build_params={
                    'task': json.dumps(task_info)
                }
            )
            return {
                'msg': 'ok'
            }


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
