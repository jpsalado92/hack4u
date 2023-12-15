FROM archlinux

# Update your system's package lists and upgrade to the latest versions:
RUN pacman -Syu --noconfirm

# Get git
RUN pacman -Sy --noconfirm git

# Get js-beautify
RUN pacman -S nodejs --noconfirm npm
RUN npm install -g js-beautify