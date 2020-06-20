# flask-list-file-system

I needed something like `tree` available at an HTTP endpoint.  
I wanted something simple to consume by other utilities.  
Prettied-up html, links, etc, were not desirable.  

`python3 flask-webserver.py`  

Returns comma separated file paths recursively, relative to the path flask is run from.  
Sub paths can be specified in the HTTP request.  
A `flaskignore.py` file is exposed to allow overriding/extending ignored files in a deployment.  

Assume the following directory structure.
```
.
├── file1
├── file2
└── directory
    └── file3
```

`localhost:5000`  
yields  
`file1,file2,directory/file3,`  


`localhost:5000/directory`  
yields  
`file3,`  
