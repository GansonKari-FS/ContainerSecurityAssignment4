# Container Security – Assignment 4.4

**Full Sail University**  
**Student:** Kari Ganson  
**Project:** Container Security Assignment 4.4

## Project Overview

This project demonstrates how to create, configure, test, and improve the security of a Docker container running a Python Flask web application.

The purpose of this assignment is to gain hands-on experience with containerization, identifying security vulnerabilities, implementing security improvements, and using Docker Scout to evaluate container images.

## Technologies Used

- Python
- Flask
- Docker Desktop
- Docker Scout
- Visual Studio Code
- Git and GitHub

## Application Description

I developed a basic Python Flask web application featuring a login interface. The application allows users to enter login credentials, authenticate, and access a successful login page.

I tested the application locally before building and running it inside a Docker container.

## Docker Configuration

I created a Dockerfile that defines the environment needed to run the Flask application.

The Dockerfile includes instructions to:

1. Use an official Python base image.
2. Establish the application's working directory.
3. Copy and install the required Python dependencies.
4. Copy the application files into the container.
5. Create a non-root user to improve container security.
6. Expose port 8080.
7. Start the Python Flask application.

## Security Improvements

### 1. Running as a Non-Root User

One important security improvement was configuring the Docker container to run as a non-root user named `appuser`.

I verified this configuration using the following command:

```bash
docker run --rm --entrypoint id container-security-app:secure
```

The command returned:

```text
uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)
```

This confirms that the container is configured to execute under a non-root account.

### 2. Updating the Python Base Image

The original Docker image used:

```dockerfile
FROM python:3.11-slim
```

I updated the Dockerfile to use:

```dockerfile
FROM python:3.13-slim
```

I then rebuilt the image to evaluate whether the updated Python version reduced the number of reported vulnerabilities.

### 3. Excluding Unnecessary Files

I created `.dockerignore` and `.gitignore` files to exclude unnecessary files and directories, including the Python virtual environment, cache files, and local environment files.

This helps reduce unnecessary build content and prevents local development files from being committed to the repository.

## Docker Scout Vulnerability Analysis

I used Docker Scout to analyze the security vulnerabilities present in the container images.

### Original Image

**Image:** `container-security-app:secure`

**Base Image:** `python:3.11-slim`

Docker Scout reported:

- Critical vulnerabilities: 0
- High vulnerabilities: 7
- Medium vulnerabilities: 12
- Low vulnerabilities: 36
- Total vulnerabilities: 55

### Updated Image

**Image:** `container-security-app:updated`

**Base Image:** `python:3.13-slim`

Docker Scout reported:

- Critical vulnerabilities: 0
- High vulnerabilities: 11
- Medium vulnerabilities: 8
- Low vulnerabilities: 35
- Total vulnerabilities: 54

### Comparison and Findings

Updating the Python base image reduced the total number of reported vulnerabilities from 55 to 54.

However, the number of high-severity vulnerabilities increased from 7 to 11.

This demonstrates that upgrading a base image does not automatically eliminate security vulnerabilities or guarantee an improvement across every severity category.

Docker Scout provided valuable information about vulnerable packages and potential security risks that require further investigation.

Additional dependency updates and vulnerability remediation would be necessary before considering the application production-ready.

## Testing and Verification

During development, I successfully:

- Created and tested the Flask application locally.
- Verified that the login interface loaded correctly.
- Confirmed successful login functionality.
- Built Docker images using the Docker CLI.
- Ran the application inside a Docker container.
- Verified the non-root user configuration.
- Analyzed the Docker images using Docker Scout.
- Compared the vulnerability reports before and after updating the base image.
- Committed the project files using Git.
- Uploaded the project to GitHub.

## Running the Application

To build the updated Docker image:

```bash
docker build -t container-security-app:updated .
```

To run the application:

```bash
docker run --rm -p 8080:8080 container-security-app:updated
```

Open a browser and navigate to:

http://127.0.0.1:8080

## Important Security Considerations

This project was developed as an educational demonstration and is not intended to serve as a production-ready authentication system.

Before deploying the application publicly, additional security measures would be necessary, including secure credential management, stronger authentication controls, dependency vulnerability remediation, and a production-ready application server.

## Conclusion

Completing this assignment helped me better understand the importance of container security and how Docker can be used to package and deploy applications consistently.

One of the most valuable lessons I learned was that updating software does not necessarily eliminate all security risks. Although the updated Python image slightly reduced the total number of vulnerabilities, some higher-severity vulnerabilities remained.

I also learned how running containers as non-root users can reduce security risks and why it is important to scan container images regularly.

Overall, this project provided practical experience with Docker, Python, container security, vulnerability analysis, and GitHub version control.

## GitHub Repository

https://github.com/GansonKari-FS/ContainerSecurityAssignment4
