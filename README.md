[![Build Status](https://travis-ci.org/sukujgrg/aflaskapp.svg?branch=master)](https://travis-ci.org/sukujgrg/aflaskapp)
# aflaskapp
a flask app

### Tested only with following (see the notes if your development and server platforms are totaly different)
1. `ubuntu 14.04`
2. `python 2.7`

### How to use this "aflaskapp"
#### After finishing these steps, you will get a self-contained pex file and a python package in a directory named `dist`
1. clone the repository `$ git clone https://github.com/sukujgrg/aflaskapp.git`
2. `$ cd aflaskapp`
3. `$ virtualenv .venv`
4. `$ export PATH=$(pwd)/.venv/bin:$PATH`
5. `$ source .venv/bin/activate`
6. `$ pip install tox`
7. `$ tox .`

### Skip to next if you want to run your app inside docker (running inside docker have its on benefits)
#### Use following command to run your `aflaskapp` from your local machine
1. `PEX_SCRIPT=gunicorn dist/aflaskapp-0.2.0.pex aflaskapp.app:app -b :8000 -D` 

### How to make use of `Dockerfile` included in the repo
1. `$ cd aflaskapp`
2. `$ docker build -t aflaskapp:latest .`
3. `$ docker images` to see all the images
4. `$ docker run -dit -p 8000:8000 aflaskapp:latest`
5. or `$ docker run -dit -p 8000:8000 aflaskapp:latest --workers=4` (entrypoint is gunicorn and so this container can accept all gunicorn parameters)

### How to access the app
1. `$ curl http://0.0.0.0:8000/customers`

#### Notes
1. `$ tox` will do all the tests mentioned in `testing/testing.py` and create a `pex` file in `dist/` with name `aflaskapp-0.2.0.pex` 
2. the flaskapp will run behind a `gunicorn` server with two worker process in the container
3. in the build system (eg. jenkins) we need to do two separate tasks on trigger. 1) creating a pex file using tox (which will do all the **`unittests`**) and 2) building a docker image and pushing it to a docker registry
4. in the deployment we need to pull the docker image
5. the benefits of creating a `pex` file are, 1) its clean 2) app is not completly dependent on docker
6. The PEX file generated in this `setup.py` via `tox` won't work on multi-platform?
  1. When you run `tox`, the `pex` file getting generated is not prepared to run on multiplatform. Following are few solutions to solve this problem
    1. Generate `pex` file which is prepared to run on multiplatform ([read](http://stackoverflow.com/questions/34979100/pants-includes-os-x-specific-python-wheels))
    2. Create `Docker` build env
7. docker image is available - `$ docker pull sukujgrg/aflaskapp`
