
build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker compose down

rebuild:
	docker compose build --no-cache

logs:
	docker compose logs -f

restart:
	stop build start