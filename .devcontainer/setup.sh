#!/usr/bin/env bash

SUDO=sudo

### Enable exit on error ######################################################
set -e

### Update package manager cache ##############################################
export DEBIAN_FRONTEND=noninteractive
$SUDO apt-get update -y


### Install poetry inside pipx ################################################
$SUDO python -m pip install pipx
$SUDO python -m pipx install poetry
$SUDO pipx ensurepath
export PATH="$PATH:$HOME/.local/bin" # Works at least for root. That's fine for docker/devcontainers


### Make available drawio in headless mode ####################################

# Install necessary libraries
$SUDO apt-get install -y libasound2

# Install drawio
if which drawio; then
    echo "drawio is already installed"
else
    drawio_package=drawio-amd64-24.4.13.deb
    curl -L -o $drawio_package https://github.com/jgraph/drawio-desktop/releases/download/v24.4.13/$drawio_package
    $SUDO apt install -y ./$drawio_package
    rm $drawio_package
fi

# Install virtual X-Server
$SUDO apt-get install -y xvfb


### Install java needed by plantuml ###########################################

$SUDO sudo apt install -y default-jre


### Install mermaid command line tool #########################################

# Install nodejs (brings package manager npm with it)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash
$SUDO apt-get install -y nodejs

# Install mermaid
$SUDO npm install -g @mermaid-js/mermaid-cli
mmdc --version

### Reload environment (variables) ############################################

source ~/.bashrc


### EOF #######################################################################

