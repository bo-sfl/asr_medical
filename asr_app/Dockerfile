# reference: https://hub.docker.com/_/ubuntu/
FROM ubuntu:18.04

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="SFL"

##Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git-core git mercurial subversion \
    build-essential \
    gcc \
    byobu \
    curl \
    htop \
    libcupti-dev \
    libfreetype6-dev \
    libzmq3-dev \
    pkg-config \
    python-pip \
    python-dev \
    python-virtualenv \
    rsync \
    software-properties-common \
    nano \
    unzip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# Install MiniConda
RUN curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda.sh && \
    bash ~/miniconda.sh -bfp /usr/local && \
    rm ~/miniconda.sh
# Update Conda
RUN conda update -y -n base conda

ENV PATH /opt/conda/bin:$PATH

## Setup File System
RUN mkdir asr
WORKDIR /asr
ADD requirements.txt /asr/
RUN pip install -r requirements.txt
ENV HOME=/asr
ENV SHELL=/bin/bash
VOLUME /asr
ADD env.yml /asr/
ADD . /asr/

## INITIALIZE CONDA ENVIRONMENT
COPY env.yml /asr/env.yml

RUN conda env create -f env.yml

# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "$SSH_PASSWD" | chpasswd

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 8000 2222
#CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["init.sh"]
