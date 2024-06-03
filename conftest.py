from pytest_metadata.plugin import metadata_key
import pytest
from tests.read_csv import writing_file, conf

output =[]

@pytest.hookimpl
def pytest_runtest_setup(item):
    tc_name = item.callspec.params['site']
    print(f'Executing the test case data {tc_name}')
   

@pytest.hookimpl
def pytest_report_teststatus(report, config):
    if report.when == 'call':
        tc_name = report.head_line.split('[')[1].split('-')[1].replace(']',"")
        if 'about:blank' in report.longreprtext:
            output.append([tc_name , 'blank'])
        else:
            output.append([tc_name , report.outcome])
        print(f'Test case name {tc_name} as status: {report.outcome}')


@pytest.hookimpl
def pytest_sessionstart(session):
    print("Test session is starting")

@pytest.hookimpl
def pytest_sessionfinish(session):
    file_name = conf()['output_filename']
    writing_file(output, f'files/{file_name}')


#@pytest.hookimpl
#def pytest_exception_interact(node, call, report):
 #   if 'ERR_EMPTY_RESPONSE' in call.excinfo.value.message:
        # Customize the way that MyCustomException is handled
  #      report.outcome = "empty_response"
  #  elif 'ERR_SSL_VERSION' in call.excinfo.value.message:
   #     report.outcome = "ssl_version"

        