cwd = $(shell pwd)
base_name = $(shell pwd | xargs basename)
user = $(shell whoami)

# make build
build:
	docker build -t ${base_name} .
# make run
run:
	docker run -i -t --name ${base_name} --restart unless-stopped -v ${cwd}/${base_name}:/app -p 8080:8000  -d ${base_name} /bin/bash
# make exec
exec:
	docker exec -i -t ${base_name} /bin/bash
# stop
stop:
	docker stop ${base_name}
# rm
remove:
	docker rm ${base_name}
