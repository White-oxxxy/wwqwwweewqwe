DC = docker-compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
STORAGES_FILE = docker_compose/storages.yaml
REDIS_FILE = docker_compose/redis.yaml
APP_FILE = docker_compose/app.yaml

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d
	# docker-compose -f docker_compose/storages.yaml --env-file .env up --build -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down
	# docker-compose -f docker_compose/storages.yaml --env-file .env up down

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d
	# docker-compose -f docker_compose/app.yaml --env-file .env up --build -d

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} ${ENV} down
	# docker-compose -f docker_compose/app.yaml --env-file .env up down

.PHONY: redis
redis:
	${DC} -f ${REDIS_FILE} ${ENV} up --build -d
	# docker-compose -f docker_compose/redis.yaml --env-file .env up --build -d

.PHONY: redis-down
redis-down:
	${DC} -f ${REDIS_FILE} ${ENV} down
	# docker-compose -f docker_compose/redis.yaml --env-file .env up down

.PHONY: logs-app
logs-app:
	${DC} logs app

.PHONY: logs-redis
logs-redis:
	${DC} logs redis

.PHONY: logs-storages
logs-storages:
	${DC} logs storages