# flask-list-file-system

I needed something like `tree` available at an HTTP endpoint.

Returns comma separted file paths recursively, relative to the path flask is run from.
Paths can be specified in the HTTP request.

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
`./file1,./file2,./directory/file3,`


`localhost:5000/directory`
yields
`./file3,`
