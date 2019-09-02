#deploy the flask UI

az webapp up -n FlaskUI

# az webapp deployment source config --name $webapp \
#   --resource-group miniproject --branch master --manual-integration \
#   --repo-url https://github.com/gadande/asr_medical/tree/master/src/azure
