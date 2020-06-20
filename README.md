# flask-list-file-system

I needed something like `tree` available at an HTTP endpoint.
I wanted something simple to consume by other utilities.
Prettied-up html, links, etc, were not desirable.

Returns comma separted file paths recursively, relative to the path flask is run from.
Sub paths can be specified in the HTTP request.

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
