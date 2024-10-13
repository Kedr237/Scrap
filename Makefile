up:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans

stop:
	docker compose -f docker-compose.yml stop

logs:
	docker compose -f docker-compose.yml logs