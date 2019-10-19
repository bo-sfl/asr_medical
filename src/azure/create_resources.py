import os
import time
import sys
import subprocess

# before running, make sure the bash files are executable: chmod u+rx *.sh

print("create resource group")
subprocess.call("create_resources/create_resource_grp.sh", shell=True)

print("Create account storage")
subprocess.call("create_resources/create_storage_acc.sh", shell=True)

print("Get storage account key")
output = subprocess.check_output("az storage account keys list -g miniproject \
  -n all2sflminiproject --query [0].value --output tsv", shell=True)
f = open("create_resources/storage_acc_key.txt", "w")
f.write("blobStorageAccountKey=%s" %output[:-1].decode('utf-8'))
f.close()
time.sleep(5)

print("Create blob containers")
subprocess.call("create_resources/create_blob_containers.sh")

print("Create app service plan")
subprocess.call("create_resources/create_app_service_plan.sh", shell=True)

print("Create Deployment user")
subprocess.call("create_resources/deployment_user.sh", shell=True)

print("Create empty webapp")
subprocess.call("create_resources/create_webapp.sh", shell=True)
