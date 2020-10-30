generate:
	java -jar scripts/openapi-generator.jar generate -i swagger.yaml -g python-flask --additional-properties=packageName=swagger_server

build:
	docker-compose build

run:
	docker-compose up

load_db:
	docker run --rm -v ${PWD}/backups:/backups:ro -v ${PWD}/data:/var/lib/neo4j/data neo4j neo4j-admin load --from=/backups/init.db.bak --force

type_check:
	mypy swagger_server

test_db:
	docker run --rm -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=none neo4j

test:
	pytest

clean:
	docker system prune -f --volumes
