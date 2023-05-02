# algorithms
### Repository for Algorithm Implementations
**Includes:**
- Dijkstra's Shortest Path
- Floyd Warshall's All Pairs Shortest Path

## requirements.txt
Install requirements with ```pip3 install -r requirements.txt```

[Using the requirements.txt](https://note.nkmk.me/en/python-pip-install-requirements/)

## linter
Run linter with command: ```pylint $(git ls-files '*.py')```
You can also run black with command: ```black .```
And/or run ```mypy .```

## Dijkstra
Maintain a table of three columns, with a row for each node.
The columns are "Node", "Shortest distance from eg. A", "Previous Node"

1. Create two lists, one of visited nodes and one of unvisited nodes
2. Select a starting node
3. Note down all distances as infinity
4. Update the connecting vertices weights and previous node
5. Remove starting node from list of unvisited.
6. Select node from unvisited nodes-list with smallest weight in table, repeat 4. and 5.
