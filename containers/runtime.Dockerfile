FROM docker.io/library/archlinux:latest

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen

RUN pacman -Syu --noconfirm

RUN pacman -S --noconfirm git blender godot

RUN ln -s /usr/bin/distrobox-host-exec /usr/bin/podman


