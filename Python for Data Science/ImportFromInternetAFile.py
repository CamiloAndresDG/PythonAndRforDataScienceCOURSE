# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:18:49 2021

@author: CamiloDiazG
"""

#De esta manera se importan archivos de internet
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)
