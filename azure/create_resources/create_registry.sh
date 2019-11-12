#!/bin/bash

# create the registry and deploy container
az acr create --resource-group miniproject --name registryasr --sku Basic --admin-enabled true
#

az acr credential show --name registryasr

sudo docker login registryasr.azurecr.io --username registryasr
# sudo az acr login --name registryasr

#
sudo docker tag asr registryasr.azurecr.io/asr:v1.0
#
sudo docker push registryasr.azurecr.io/asr:v1.0
#
sudo az acr repository list --name registryasr --output table
#
# az container create --resource-group miniproject --name deepspeech --image registryasr.azurecr.io/deepspeech:v1.0 --cpu 1 --memory 1 --registry-login-server registryasr.azurecr.io --registry-username registryasr --registry-password <acrPassword> --dns-name-label <aciDnsLabel> --ports 80
