# hack4u

Multi-container environment for development and testing pentesting tools.

## Docker Compose

The `docker-compose.yml` file is used to define and manage the multi-container Docker environment for this project.

It specifies the services, networks, and volumes required for the application.

The file defines:
- Two services `attacker-archlinux` and `victim-ubuntu`.
- A network `hack4u-network` for the services to communicate with each other.
- A volume `workspace` to share files between the host and the services.

### attacker-archlinux
This service is built from the Dockerfile located at `.devcontainer/attacker-archlinux/Dockerfile`.
The Dockerfile specifies the steps to create a Docker image with **Arch Linux** and the necessary tools for the attacker environment.
The `attacker-archlinux` service is connected to the `hack4u-network` network and has the project root directory mounted as a volume at /workspace.

### victim-ubuntu
This service is built from the Dockerfile located at `.devcontainer/victim-ubuntu/Dockerfile`.
The Dockerfile specifies the steps to create a Docker image with Ubuntu and the necessary tools for the victim environment.
The victim-ubuntu service is also connected to the `hack4u-network` network and has the project root directory mounted as a volume at /workspace.
