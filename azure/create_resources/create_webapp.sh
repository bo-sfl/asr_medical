# create the web app
webapp=sfl-all-asr-app

az webapp create --resource-group miniproject --plan MiniProjectApp --name $webapp --deployment-container-image-name registryasr.azurecr.io/asr:v1.0


# az webapp create --name $webapp --resource-group miniproject --plan MiniProjectApp \
#   --runtime "python|3.6" --deployment-local-git

# configure registry credentials
az webapp config container set --name $webapp --resource-group miniproject --docker-custom-image-name registryasr.azurecr.io/asr:v1.0 --docker-registry-server-url https://registryasr.azurecr.io --docker-registry-server-user registryasr --docker-registry-server-password =RZuEu4Dtx7Q6LsB5u53i5ByGOl3nVBw


# configure environment variables
az webapp config appsettings set --resource-group miniproject --name $webapp --settings WEBSITES_PORT=8000
