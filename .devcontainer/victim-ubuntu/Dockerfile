FROM ubuntu:22.04

# Update package list
RUN apt-get update

# Install Git
RUN apt-get install -y git

# Prettier bash prompt
RUN echo "PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc

# Install Firefox
RUN apt-get install bzip2 wget
RUN apt-get install -y ffmpeg
RUN apt-get install -y libpci3 libegl1-mesa libgl1-mesa-glx libasound2 libgtk-3-0 libx11-6 libx11-xcb1 libxt6
RUN wget -O FirefoxSetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
RUN tar xjf FirefoxSetup.tar.bz2 -C /opt/
RUN ln -s /opt/firefox/firefox /usr/bin/firefox
RUN rm FirefoxSetup.tar.bz2
