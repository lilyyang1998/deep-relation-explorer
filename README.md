# Deep Relation Explorer

### Paper abstract:
- We use the Wikidata to construct relations between two names, and evaluate the correlation
- Explore relation on an open-domain knowledge base

### Project structure:
```
relation_extraction/
├── relextserver
│   ├── server.py
│   └── static/
│       ├── index.html
│       ├── main.css
└──     └── main.js
```

<table>
    <tr>
        <th>File</th><th>Description</th>
    </tr>
    <tr>
        <td>relation_extraction/relextserver</td><td>The code for the web demo.</td>
    </tr>
</table>

### Setup:

1. We recommend that you setup a new pip environment first: http://docs.python-guide.org/en/latest/dev/virtualenvs/

2. Check out the repository and run:
```
pip install -r requirements.txt
```

3. Run the following command to execute the website:
```
python runserver.py