#!/bin/bash

# Send Latest Scripts to Production Server
rsync -avz scripts/ $PROD_SERVER:/var/www/zadacha/scripts/
# TODO add /etc rsync -avz etc/ $PROD_SERVER:/var/www/zadacha/etc/
scp docker-compose.yml $PROD_SERVER:/var/www/zadacha

# Log into Production Server, Pull and Restart Docker
ssh $PROD_SERVER 'cd /var/www/zadacha && docker-compose pull'
ssh $PROD_SERVER 'cd /var/www/zadacha && docker-compose build'
ssh $PROD_SERVER 'cd /var/www/zadacha && source scripts/secrets.sh && docker-compose up -d'