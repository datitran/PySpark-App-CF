#!/usr/bin/env bash

SPARK_URL=http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
SPARK_FILENAME=spark-2.1.0-bin-hadoop2.7.tgz

set -e

echo "Hello World"

apt-get update
apt-get -y install wget curl software-properties-common

# install openjdk
add-apt-repository -y ppa:openjdk-r/ppa
apt-get update
apt-get -y install openjdk-8-jdk

# Install Miniconda
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh \
    && /bin/bash ~/miniconda.sh -b -p $HOME/conda

echo -e '\nexport PATH=$HOME/conda/bin:$PATH' >> $HOME/.bashrc && source $HOME/.bashrc

# install Packages
conda install -y nose numpy pandas

# Install Spark
curl $SPARK_URL > $HOME/$SPARK_FILENAME
tar -xzf $HOME/$SPARK_FILENAME -C $HOME/

echo 'export SPARK_HOME=$HOME/spark-2.1.0-bin-hadoop2.7/' >> $HOME/.bashrc && source $HOME/.bashrc

nosetests -vs pyspark-app-ci/tests/test_linear_regression.py

# show folders
find .