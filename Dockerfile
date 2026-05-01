FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm install -g turbo
RUN npm install
CMD ["npm", "run", "dev"]
