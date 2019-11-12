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

## Setup File System
RUN mkdir deepspeech
ENV HOME=/deepspeech
ENV SHELL=/bin/bash
VOLUME /deepspeech
WORKDIR /deepspeech

## INITIALIZE CONDA ENVIRONMENT
COPY deepspeech.yml /deepspeech/deepspeech.yml
COPY . /deepspeech
RUN conda env create -f deepspeech.yml
ENV PATH /usr/local/envs:$PATH

# Open Ports
EXPOSE 5000
