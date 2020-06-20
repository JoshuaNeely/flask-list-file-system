import os
from flask import Flask
app = Flask(__name__)


IGNORE_DIRECTORIES = ['.git', '__pycache__']


@app.route('/')
def directory_contents():
  return ','.join( list_dir_recursive('.') )

@app.route('/<path:subpath>')
def directory_contents_path(subpath):
  return ','.join( list_dir_recursive(subpath) )


def list_dir_recursive(directory):
  directory_contents = os.listdir(directory)

  files = [f for f in directory_contents if os.path.isfile(os.path.join(directory, f))]
  directories = [d for d in directory_contents if not os.path.isfile(os.path.join(directory, d))]
    
  filtered_directories = [ d for d in directories if d not in IGNORE_DIRECTORIES ]
  for d in filtered_directories:
    recursive_files = list_dir_recursive('{}/{}'.format(directory,d))
    prepended_with_directory = list(map(lambda x: '{}/{}'.format(d, x), recursive_files))
    files += prepended_with_directory

  return files
