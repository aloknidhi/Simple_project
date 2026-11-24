FROM node:20-alpine

WORKDIR /app

ENV CHOKIDAR_USEPOLLING=true

COPY package.json ./
RUN npm install

COPY . . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
