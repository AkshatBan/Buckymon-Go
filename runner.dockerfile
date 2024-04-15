FROM gitlab/gitlab-runner:alpine

# Update the repos where it will look for deps
RUN apk update
# Install Node.js
RUN apk add --no-cache nodejs npm
#Install python
RUN apk add python3
#Install mysql and client
RUN apk add mysql mysql-client

# Install Docker
RUN apk add --no-cache docker-cli

# Install any other dependencies you may need for your GitLab Runner setup
