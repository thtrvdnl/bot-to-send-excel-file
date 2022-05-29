project_name := filebot
compose_file := docker-compose.yml
compose := docker-compose -p $(project_name) -f $(compose_file)

bu: build_and_install
build_and_install:
	$(compose) up -d --build $(service)

gc: generate_configs
generate_configs:
	cp configs/bot.env.example configs/bot.env

create_network:
	docker network create filebot

style:
	black .
	isort .
