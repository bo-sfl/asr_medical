Deploying Flask App on Azure:


0. in src/azure, Run the script:
```python create_resources.py```

It will launch the following formation scripts:

    1. create resource group:
    . create_resources/create_resource_grp.sh

    2. Create account storage:
    . create_resources/create_storage_acc.sh

    3. Create app service plan:
    . create_resources/create_app_service_plan.sh

    4. Create Deployment user:
    . create_resources/deployment_user.sh

    5. Create empty webapp:
    . create_resources/create_webapp.sh

When prompted, enter a password (this password will be the one to push app in the following steps)

6.Deploy webapp from local git folder

(Temporary) In the Azure console, get to the storage account -> storage key and copy the first key.
Paste the key into src/azure/asr_app/process.py in the accountKey variable

within asr_app folder:
git init
git add .
git commit -am "az flask app"
#git remote add azure https://<app_url>
git push azure master

7. In the console, in the app configuration - general settings, specify startup command:
"python application.py"
