# create the web app
webapp=sfl-all-asr-app

az webapp create --name $webapp --resource-group miniproject --plan MiniProjectApp \
  --runtime "python|3.6" --deployment-local-git
