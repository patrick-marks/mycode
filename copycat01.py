#!/usr/bin/env/ python3

# import additional code to complete our task
import shutil

import os

# move into the working directory
os.chdir("/home/student/mycode")

# copy to the fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

shutil.copytree("5g_research/", "5g_research_backup/")


