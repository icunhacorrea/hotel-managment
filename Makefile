build:
	docker compose build --no-cache

up:
	docker compose up -d

migrate:
	docker compose exec webserver python hotel_managment/manage.py migrate

makemigrations:
	docker compose exec webserver python hotel_managment/manage.py makemigrations

start_app:
	docker compose exec webserver python hotel_managment/manage.py startapp $(name)

stop:
	docker compose stop

logs:
	docker compose logs -f

createsuperuser:
	docker compose exec webserver python hotel_managment/manage.py createsuperuser

clean:
	docker system prune -f
	docker volume prune -f
	rm hotel_managment/db.sqlite3
