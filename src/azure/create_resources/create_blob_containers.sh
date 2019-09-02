#!/bin/bash

# create blob storage containers (folders)
source create_resources/storage_acc_key.txt
blobStorageAccount=all2sflminiproject

# blobStorageAccountKey=$(az storage account keys list -g miniproject \
#   -n $blobStorageAccount --query [0].value --output tsv)

az storage container create -n raw8audio --account-name $blobStorageAccount \
  --account-key $blobStorageAccountKey --public-access off

sleep 3

az storage container create -n processed8audio --account-name $blobStorageAccount \
  --account-key $blobStorageAccountKey --public-access off
