# How to set up a CI/CD Pipeline YAML file
## In GitLab, specifically
### Naming
For GitLab, specifically, the YAML file needs to be named ".gitlab-ci.yml".
### Runners
GitLab requires users to set up runners in the CI/CD part of the project settings. These runner scripts are responsible for running the jobs specified in the yaml script.
For more information on setting up runners, read the relevant section of the GitLab page linked in the More Information section.
### Setting up the YAML file
Go to Code > Repository and create a YAML file. Leave the branch to commit to as "main".
## What should a YAML file look like?
### General guidelines
The YAML file has the following general pattern: Build, Test, Deploy. The build step is responsible for setting up all the dependencies for the project to run and compile. The test step is responsible for running the developed unit tests on the code. The deploy step takes over once the code is successfully built and tested. This step makes the application live and available to use.
### Our template
In our YAML file, we will split up the build job into three parts: build-frontend, build-backend, and build-database. The build steps should be run on every branch, as we want to make sure that new changes don't mess up the compilation. Building is also important for testing.

The testing job will run all the unit tests on the entire code as part of the current build. We also want to run this on every branch. That way, we have some sort of regression testing to make sure new code hasn't broken some previous functionality.

The deployment job will only run on the main branch. We don't need to make our application live for every commit.

## More information
[GitLab's pipeline tutorial](https://docs.gitlab.com/ee/ci/quick_start/)