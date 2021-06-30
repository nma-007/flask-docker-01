# flask-docker-01
example flask run on docker build, run, and *publish

docker build -t docker_flask:latest .

docker run -d -p 80:5000 docker_flask:latest

docker push docker_flask:latest


