# pull official base image
FROM nginx:1.21-alpine

# Delete default nginx website and copy our own
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d