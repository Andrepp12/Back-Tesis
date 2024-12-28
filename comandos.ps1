docker build -t andrepp/back-tesis:latest .

docker rm -f andrepp-back-tesis
docker run -d --env-file=.env -p 8000:8000 --name andrepp-back-tesis --network andrepp andrepp/back-tesis:latest