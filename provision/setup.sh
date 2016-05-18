#!/usr/bin/env bash

# Vagrant Java Development Box provision

cat << EOF | sudo tee -a /etc/motd.tail
***************************************

Welcome to Vagrant Development Box provision

***************************************
EOF

### Fix for mac issue on UTF-8
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
locale-gen en_US.UTF-8
dpkg-reconfigure locales

### Common Package Install
echo "Updating Repo"
sudo apt-get update
echo "Installing Essential Packages"
sudo apt-get install -y python-software-properties build-essential > /dev/null
echo "Installing curl vim zip unzip python pip"
sudo apt-get install -y curl vim zip unzip python-pip git > /dev/null


### Install java
sudo echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
sudo echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
sudo apt-get update
sudo apt-get install -y software-properties-common python-software-properties
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
sudo apt-get install -y oracle-java8-installer ca-certificates

### echo success message
echo "You've been provisioned"