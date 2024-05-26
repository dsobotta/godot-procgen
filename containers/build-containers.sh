#!/bin/bash

podman build -t runtime -f runtime.Dockerfile

podman build -t dev -f dev.Dockerfile

distrobox assemble create --replace --file ./distrobox.ini
