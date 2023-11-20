#!/bin/bash

# Update package list
apt-get update

# Get tmux
apt install tmux -y

# Get ohmytmux
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .


# Get zsh
apt install zsh -y

# Get ohmyzsh
yes Y | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh) -y" 
clear

# Set zsh as default shell
chsh -s /bin/zsh 