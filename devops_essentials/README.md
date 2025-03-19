# Containerization and Orchestration Essentials

## Description
This project is designed to immerse students in the fundamentals of containerization and orchestration using Docker, Docker Compose, and GitHub Actions. Through a series of hands-on tasks, students will gain practical experience in creating, customizing, and deploying Docker images, managing data persistence, and orchestrating simple multi-service infrastructures. The project adopts a learn-by-doing approach, encouraging students to leverage provided resources, explore solutions independently, and collaborate to overcome challenges.

## Files

| Filename | Description |
|----------|------------|
| `Dockerfile` | Contains instructions to create a basic Docker image based on the Alpine image, printing “Hello, World!” when run. |
| `config.txt` | A configuration file containing the text “Welcome to Docker!”, used in the extended Docker image setup. |
| `docker-image.yml` | GitHub Actions workflow file for automating the build and push process of the Docker image to GitHub Container Registry. |
| `docker-compose.yml` | Docker Compose file that defines a multi-container environment with PostgreSQL and pgAdmin, allowing easy orchestration and inter-service communication. |