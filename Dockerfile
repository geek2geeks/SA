# Stage 1: Build the React application
FROM node:14 AS build

# Set the working directory
WORKDIR /usr/src/app

# Copy the frontend directory into the Docker image
COPY ./ana/frontend .

# Install dependencies and build the project
RUN npm install
RUN npm run build

# Stage 2: Serve the React application using Nginx
FROM nginx:alpine

# Copy the build directory from the previous stage to the Nginx HTML directory
COPY --from=build /usr/src/app/build /usr/share/nginx/html

# Expose port 80 for HTTP
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
