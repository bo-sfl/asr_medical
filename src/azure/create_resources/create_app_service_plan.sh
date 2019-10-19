#!/bin/bash

#create app service plan
az appservice plan create --name MiniProjectApp --resource-group miniproject --sku Free \
  --is-linux
