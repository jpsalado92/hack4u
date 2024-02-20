FROM archlinux

# Update your system's package lists and upgrade to the latest versions:
RUN pacman -Syu --noconfirm

# Get git
RUN pacman -Sy --noconfirm git

# Get js-beautify
RUN pacman -S nodejs --noconfirm npm
RUN npm install -g js-beautify

# Get python packages
# - Get pip
# - Get ruff
# - Get tkinter
# - Get scapy
# - Get python-termcolor
RUN pacman -Sy --noconfirm python-pip
RUN pacman -Sy --noconfirm python-ruff
RUN pacman -Sy --noconfirm tk
RUN pacman -Sy --noconfirm scapy
RUN pacman -Sy --noconfirm xorg-fonts-100dpi
RUN pacman -Sy --noconfirm python-termcolor

# Get netcat
RUN pacman -Sy --noconfirm gnu-netcat


# Get xxd
RUN pacman -Sy --noconfirm xxd

# Get wireshark
# - Get only the CLI version of wireshark
# - Grant necessary capabilities to dumpcap
RUN pacman -Sy --noconfirm wireshark-cli
RUN pacman -Sy --noconfirm libcap
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

# Clear cache
RUN pacman -Scc --noconfirm


# Prettier bash prompt
RUN echo "PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc