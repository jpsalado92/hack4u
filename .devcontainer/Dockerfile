FROM archlinux

# Update your system's package lists and upgrade to the latest versions:
RUN pacman -Syu --noconfirm

# Get git
RUN pacman -Sy --noconfirm git

# Get js-beautify
RUN pacman -S nodejs --noconfirm npm
RUN npm install -g js-beautify

# Get python-pip
RUN pacman -Sy --noconfirm python-pip

# Get python-ruff
RUN pacman -Sy --noconfirm python-ruff

# Get netcat
RUN pacman -Sy --noconfirm gnu-netcat

# Get tkinter for python
RUN pacman -Sy --noconfirm tk
RUN pacman -Sy --noconfirm xorg-fonts-100dpi

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
