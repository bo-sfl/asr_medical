import os
import time
import sys
import subprocess

# before running, make sure the bash files are executable: chmod u+rx *.sh

print("create resource group")
subprocess.call("create_resources/create_resource_grp.sh", shell=True)

print("Ceate container Registry")
subprocess.call("create_resources/create_registry.sh", shell=True)

print("Create app service plan")
subprocess.call("create_resources/create_app_service_plan.sh", shell=True)

print("Create web app")
subprocess.call("create_resources/create_webapp.sh", shell=True)
