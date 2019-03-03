#!/usr/bin/env bash

docker run -d --name bioformats -p 8000:8000 -v $PWD/notebooks:/usr/src -w /usr/src --rm bioformats && sleep 2 && open http://localhost:8000 && echo "Done. Chiki"
