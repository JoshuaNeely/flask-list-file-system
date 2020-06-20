import os
import pytest

import flask_webserver


@pytest.fixture
def client():
  flask_webserver.app.config['TESTING'] = True

  with flask_webserver.app.test_client() as client:
    with flask_webserver.app.app_context():
      yield client


def test_recursive_file_search(client):
  '''Test directory recursion'''

  response_data = client.get('/tests/mock-file-system').data
  assert b'test1' in response_data
  assert b'test2' in response_data
  assert b'test-dir/test3' in response_data


def test_recursive_file_search_shortcut(client):
  '''Test ability to specify subpath'''

  response_data = client.get('/tests/mock-file-system/test-dir').data
  assert response_data == b'test3'
