# Project 2 - Dockerized Nginx

This project runs a custom Nginx container with a simple HTML page.

## Files
- **Dockerfile**: Builds a custom Nginx image based on `nginx:alpine`.
- **index.html**: Custom homepage.
- **README.md**: Documentation.

## Build and Run
```bash
docker build -t my-nginx .
docker run -d -p 8080:80 my-nginx
