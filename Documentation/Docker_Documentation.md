# Docker Documentation
This guide will go through all information docker related to this project.
## How to upload your images to the registry for this project?
Uploading custom Images follows the following format:
### Create a Dockerfile

[`ADD`](https://docs.docker.com/reference/dockerfile/#add)   Add local or 
remote files and directories.

[`ARG`](https://docs.docker.com/reference/dockerfile/#arg) Use build-time 
variables.

[`CMD`](https://docs.docker.com/reference/dockerfile/#cmd) Specify default 
commands.

[`COPY`](https://docs.docker.com/reference/dockerfile/#copy) Copy files 
and directories.

[`ENTRYPOINT`](https://docs.docker.com/reference/dockerfile/#entrypoint) 
Specify default executable.

[`ENV`](https://docs.docker.com/reference/dockerfile/#env) Set environment 
variables.

[`EXPOSE`](https://docs.docker.com/reference/dockerfile/#expose) Describe 
which ports your application is listening on.

[`FROM`](https://docs.docker.com/reference/dockerfile/#from) Create a new 
build stage from a base image.

[`HEALTHCHECK`](https://docs.docker.com/reference/dockerfile/#healthcheck) 
Check a container's health on startup.

[`LABEL`](https://docs.docker.com/reference/dockerfile/#label) Add 
metadata to an image.

[`ONBUILD`](https://docs.docker.com/reference/dockerfile/#onbuild) Specify 
instructions for when the image is used in a build.

[`RUN`](https://docs.docker.com/reference/dockerfile/#run) Execute build 
commands.

[`SHELL`](https://docs.docker.com/reference/dockerfile/#shell) Set the 
default shell of an image.

[`STOPSIGNAL`](https://docs.docker.com/reference/dockerfile/#stopsignal) 
Specify the system call signal for exiting a container.

[`USER`](https://docs.docker.com/reference/dockerfile/#user) Set user and 
group ID.

[`VOLUME`](https://docs.docker.com/reference/dockerfile/#volume) Create 
volume mounts.

[`WORKDIR`](https://docs.docker.com/reference/dockerfile/#workdir) Change 
working directory.

### Docker build
 The command for building a custome image will look like: `docker build -f 
Dockerfile -t myimage:latest .`

The `-f` flag specifies the Dockerfile to be used, if left blank will use 
first Dockerfile in current directory.

The `-t` flag allows tagging/naming an image helps controlling different 
version of the image.

The final `.` tells docker where to put the image, in this the current 
directory.

### Pushing images to gitlab registry
Before doing anything login to the registry for this project using `docker 
login registry.doit.wisc.edu` you will need access to your auth key. If 
you do not have your auth key generate one with full access.

Once you have an image ready you can push to the following location using 
`docker push 
registry.doit.wisc.edu/cdis/cs/courses/cs506/sp2024/team/mondaywednesdaylecture/t_01/buckymon-go/[frontend]/[image]` 
be sure to replace the `frontend` and `image` with the appropriate 
substitutions.

If that doesn't work right away, try the following command:
`docker tag my_mysql_image registry.doit.wisc.edu/cdis/cs/courses/cs506/sp2024/team/mondaywednesdaylecture/t_01/buckymon-go/my_mysql_image`
Be sure to replace `my_mysql_image` with the image name you specified above.

## Where to find Docker Images
Head over to the git lab project and you will find the images in `Deploy 
→ Container Registry`

## How to run the Docker Images in containers
* To run any any of the images in the registry, next to each image in registry there is an icon with the subtitle 'Copy Image Path'
* Head over to a terminal and do a `docker pull [image path]`
* Now that you have the image you can do docker run with that image path, but please refer to the creator of image for ports and other flags to consider while running 
