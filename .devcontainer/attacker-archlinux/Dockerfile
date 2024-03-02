FROM archlinux

# Prettier bash prompt
RUN echo "PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc

# Update your system's package lists and upgrade to the latest versions:
RUN pacman -Syu --noconfirm

# Get git
RUN pacman -Sy --noconfirm git

# Get js-beautify
RUN pacman -S nodejs --noconfirm npm
RUN npm install -g js-beautify

# Get python packages
# - Get pip
RUN pacman -Sy --noconfirm python-pip
# - Get ruff
RUN pacman -Sy --noconfirm python-ruff
# - Get tkinter
RUN pacman -Sy --noconfirm tk
# - Get scapy
RUN pacman -Sy --noconfirm scapy
# - Get python-termcolor
RUN pacman -Sy --noconfirm python-termcolor
# - Get python-scapy
RUN pacman -Sy --noconfirm python-scapy
# - Get arp-scan
RUN pacman -Sy --noconfirm arp-scan

# Get networking tools
RUN pacman -Sy --noconfirm net-tools
# - Get netcat
RUN pacman -Sy --noconfirm gnu-netcat
# - Get ipcalc
RUN pacman -Sy --noconfirm ipcalc

# Get fonts
RUN pacman -Sy --noconfirm xorg-fonts-100dpi

# Get utils
# - Get xxd
RUN pacman -Sy --noconfirm xxd

# Get wireshark
# - Get only the CLI version of wireshark
# - Grant necessary capabilities to dumpcap
RUN pacman -Sy --noconfirm wireshark-cli
RUN pacman -Sy --noconfirm wireshark-qt
RUN pacman -Sy --noconfirm libcap
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

# Get nmap
RUN pacman -Sy --noconfirm nmap

# Get macchanger
RUN pacman -Sy --noconfirm macchanger

# Clear cache
RUN pacman -Scc --noconfirm
