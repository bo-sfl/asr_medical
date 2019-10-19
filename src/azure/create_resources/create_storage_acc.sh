#!/bin/bash

# create blob storage
blobStorageAccount=all2sflminiproject

az storage account create --name $blobStorageAccount \
  --location eastus --resource-group miniproject \
  --sku Standard_LRS --kind blobstorage --access-tier hot
