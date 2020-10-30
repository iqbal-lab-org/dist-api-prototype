[![Build Status](https://travis-ci.com/iqbal-lab-org/dist-api-prototype.svg?branch=master)](https://travis-ci.com/iqbal-lab-org/dist-api-prototype)

# Usage

## Start the development server
```shell script
make build
make run
```

If you want to use the sample data, stop the server (you need the run the server at least once so it create the necessary directories), then
```
make load_db
```

## View the toy graph
* Visit http://localhost:7474
* Set `Connect URL` to `bolt://localhost:7687`
* Set `Authentication type` to `No authentication`
* Click the top left icon (Databases), it should show the currently existing node and relationship types. Click on one of them to view the graph.
* Drag the nodes far away from each other for clarity. You can also set colors for them.

## Make a test request

* Nearest neighbors
```shell script
curl --request GET 'localhost:8080/api/v1/samples/s1/nearest-neighbours'
# The result should be a JSON array of {experiement_id: str, distance: int}
```

* Nearest leaf in the phylogenetic tree
```shell script
curl --request GET 'localhost:8080/api/v1/samples/s1/nearest-leaf-node'
# The result should look like
# {
#   "distance": 7,
#   "leaf_id": "l857"
# }
```

# Development

## Run tests
```shell script
make test_db
make test
```
