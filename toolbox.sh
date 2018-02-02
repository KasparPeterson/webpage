function run {
    docker-compose build
    docker-compose up
}

function run-daemon {
    docker-compose build
    docker-compose up -d
}