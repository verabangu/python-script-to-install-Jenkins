#!/usr/bin/python3 
import os

# Update the system
os.system('sudo yum update -y')

# Install Java
os.system('sudo yum install java-1.8.0-openjdk -y')

# Add the Jenkins repository to yum
os.system('sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo')
os.system('sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key')

# Install Jenkins
os.system('sudo yum install jenkins -y')

# Start and enable the Jenkins service
os.system('sudo systemctl start jenkins')
os.system('sudo systemctl enable jenkins')

# Print the initial admin password
os.system('sudo cat /var/lib/jenkins/secrets/initialAdminPassword')
