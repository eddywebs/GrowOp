# base-image for python on any machine using a template variable,
# see more about dockerfile templates here:http://docs.resin.io/pages/deployment/docker-templates
FROM resin/raspberrypi3-python:3

# use apt-get if you need to install dependencies,
# for instance if you need ALSA sound utils, just uncomment the lines below.
# RUN apt-get update && apt-get install -yq \
#    alsa-utils libasound2-dev && \
#    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set our working directory
WORKDIR /usr/src/app

# Copy requirements.txt first for better cache on later pushes
COPY ./requirements.txt /requirements.txt

# pip install python deps from requirements.txt on the resin.io build server
RUN pip install -r /requirements.txt

#install gip 
#todo use wiringPi or move it to requirements.txt
RUN pip install RPi.GPIO

# This will copy all files in our root to the working  directory in the container
COPY . ./

#RUN cd /root && git clone https://github.com/WiringPi/WiringPi.git && cd WiringPi && ./buildf


# switch on systemd init system in container
ENV INITSYSTEM on

# main.py will run when container starts up on the device
CMD ["python","-u","src/main.py"]
