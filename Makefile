
.PHONY: start
start:
	@printf "[exec] Python Django Start!!!\n"; \
	sh deploy/local/django/settings.sh
	python manage.py runserver;

.PHONY: deploy
deploy:
	@printf "[exec] 배포 환경 (dev, prod): "; \
	read conf; \
	python deploy/deploy.py -s $$conf

.PHONY: up
up:
	@docker compose up -d --build
	
.PHONY: down
down:
	@docker compose down

.PHONY: exec
exec:
	@docker compose ps
	@printf "[exec] 서비스 이름: "; \
	read service; \
	docker compose exec $$service /bin/bash;

.PHONY: rmi
rmi:
	@docker compose down --rmi all

.PHONY: none
none:
	@docker rmi $$(docker images -a | grep "^<none>" | awk '{print $3}')

.PHONY: daemon-up
daemon-up:
	systemctl stop django.service
	sh deploy/local/django/settings.sh
	cp deploy/django.service /etc/systemd/system/django.service
	systemctl start django.service

.PHONY: daemon-down
daemon-down:
	systemctl stop django.service

.PHONY: clean
clean:
	rm -rf static log data 