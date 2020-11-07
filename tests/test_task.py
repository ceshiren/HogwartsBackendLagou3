from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins(
        'http://stuq.ceshiren.com:8020/',
        username='seveniruby',
        password='11315b2e19bd545b4f6ae16d8643d4ab18'
    )
    print(jenkins.version)
    print(jenkins.keys())
    print(jenkins['lagou3_testcase'].get_last_build().get_artifact_dict())
    jenkins['lagou3_testcase'].invoke(
        build_params={'testcase_id': 1},
        block=True
    )
    print(jenkins['lagou3_testcase'].get_last_build().get_artifact_dict())
