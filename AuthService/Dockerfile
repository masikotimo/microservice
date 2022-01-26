FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /auth_service

# Set the working directory to /auth_service
WORKDIR /auth_service

# Copy the current directory contents into the container at /auth_service
ADD . /auth_service/

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

CMD sh init.sh && pytest && python3 manage.py runserver 0.0.0.0:8000
