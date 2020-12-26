from jenkinsapi.jenkins import Jenkins

from backend import db


def test_create_table():
    db.create_all()


def test_jenkins():
    jenkins = Jenkins(
        'http://stuq.ceshiren.com:8020/',
        username='seveniruby',
        password='11fbcfb9793b526ef147258c968ce62543'
    )
    print(jenkins.keys())
    res=jenkins['lagou4_testcase'].invoke(build_params={'testcases': '123'})
    print(res)
