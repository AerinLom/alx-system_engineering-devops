0x09. Web infrastructure design

# Learning Objectives

You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
You must be able to explain what each component is doing
You must be able to explain system redundancy
Know all the mentioned acronyms: LAMP, SPOF, QPS

# Web Infrastructure Design

This repository contains designs for various web infrastructure setups, ranging from a simple one-server setup to a secured and monitored distributed infrastructure.

## Tasks

### 0. Simple Web Stack

Design a one-server web infrastructure that hosts the website `www.foobar.com`. The setup includes:

- 1 server
 - A server is a physical or virtual machine that hosts the various components required to serve web content.

- 1 web server (Nginx)
 - The web server (Nginx) receives incoming HTTP requests from users' browsers and forwards them to the application server. It also serves static content directly.

- 1 application server
 - The application server executes the application code that generates dynamic content for the website. It processes requests from the web server, interacts with the database, and generates responses.

- 1 application code base
 - The application files contain the code base for the website.

- 1 database (MySQL)
 - The database (MySQL) stores and manages the data required by the application.

- 1 domain name `foobar.com` with a `www` record pointing to the server IP `8.8.8.8`
 - The domain name `foobar.com` is a human-readable address for the website. The `www` record is a subdomain that points to the server's IP address.

### 1. Distributed Web Infrastructure

Design a three-server web infrastructure that hosts the website `www.foobar.com`. The setup includes:

- 2 additional servers
 - Adding more servers improves redundancy and scalability.

- 1 web server (Nginx)
 - The web server receives incoming requests and forwards them to the application servers.

- 1 application server
 - The application server processes requests and generates responses.

- 1 load balancer (HAproxy)
 - The load balancer distributes incoming traffic across the application servers, improving performance and availability.

- 1 application code base
 - The application files contain the code base for the website.

- 1 database (MySQL)
 - The database stores and manages the data required by the application.

### 2. Secured and Monitored Web Infrastructure

Design a three-server web infrastructure that hosts the website `www.foobar.com`, secured with encrypted traffic and monitoring. The setup includes:

- 3 firewalls
 - Firewalls control and monitor incoming and outgoing network traffic, providing security.

- 1 SSL certificate for `www.foobar.com` over HTTPS
 - The SSL certificate enables secure, encrypted communication over HTTPS, protecting sensitive data.

- 3 monitoring clients (e.g., Sumologic)
 - Monitoring clients collect and analyze data about the infrastructure's performance, availability, and security, allowing for proactive management.


## Conclusion

The designs in this repository demonstrate the evolution of web infrastructure from a simple one-server setup to a distributed, secured, and monitored environment. Each design addresses specific requirements, such as scalability, redundancy, security, and monitoring, providing a foundation for building robust and reliable web applications. These designs can serve as a starting point for further customization and optimization based on the specific needs of a project.
