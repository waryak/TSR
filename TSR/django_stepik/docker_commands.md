Launch docker container with mounted code folder

`docker run -it --mount type=bind,source=/Users/waryak/Documents/TSR/django_stepik,target=/app,readonly tsumina/nginx-python3 /bin/bash`