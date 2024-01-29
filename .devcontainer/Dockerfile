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