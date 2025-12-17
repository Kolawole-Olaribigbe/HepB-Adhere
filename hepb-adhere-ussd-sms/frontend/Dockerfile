FROM node:16 AS build

WORKDIR /app

COPY web/package.json web/package-lock.json ./
RUN npm install

COPY web/ ./
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]