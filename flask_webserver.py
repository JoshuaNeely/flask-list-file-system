import os
from flask import Flask
app = Flask(__name__)


IGNORE_DIRECTORIES = ['.git', '__pycache__']


@app.route('/')
def directory_contents():
  return list_dir_recursive('.')

@app.route('/<path>')
def directory_contents_path(path):
  return list_dir_recursive(path)


def list_dir_recursive(start_path):
  buffer = ''

  directory = start_path
  directory_contents = os.listdir(directory)

  files = [f for f in directory_contents if os.path.isfile(os.path.join(directory, f))]
  directories = [d for d in directory_contents if not os.path.isfile(os.path.join(directory, d))]
    
  for f in files:
    buffer += '{}/{},'.format(directory, f)

  filtered_directories = [ d for d in directories if d not in IGNORE_DIRECTORIES ]
  for d in filtered_directories:
    directory = '{}/{}'.format(start_path, d)
    buffer += list_dir_recursive(directory)

  return buffer;
