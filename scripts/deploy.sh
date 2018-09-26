#!/bin/bash

sudo apt install -y rsync

# Send Latest Scripts to Production Server
rsync -o StrictHostKeyChecking=no -avz scripts/ $PROD_SERVER:/var/www/zadacha/scripts/
# TODO add /etc rsync -avz etc/ $PROD_SERVER:/var/www/zadacha/etc/
scp -o StrictHostKeyChecking=no docker-compose.yml $PROD_SERVER:/var/www/zadacha

# Log into Production Server, Pull and Restart Docker
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/zadacha && docker-compose pull'
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/zadacha && docker-compose build'
ssh -o StrictHostKeyChecking=no $PROD_SERVER 'cd /var/www/zadacha && source scripts/secrets.sh && docker-compose up -d'