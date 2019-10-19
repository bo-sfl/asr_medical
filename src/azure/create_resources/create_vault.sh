#!/bin/bash

source create_resources/storage_acc_key.txt

# Register keyvault provider
az provider register -n Microsoft.KeyVault

# create keyvault
az keyvault create --name "miniprojectKeyVault" \
  --resource-group "miniproject" --location "eastus"

# add storage account secret
az keyvault secret set --vault-name "miniprojectKeyVault" \
  --name "blobStorageAccountKey" --value $blobStorageAccountKey
