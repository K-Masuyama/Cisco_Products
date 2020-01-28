# -*- coding: utf-8 -*-

# This script is for running On-Premiss CMX API. 
# "Class" is written to fit in each API method. (Please refer to https://msesandbox.cisco.com:8081/apidocs/)
# In addition, each method within classes corresponds to APIs written in above web page.
# If you have question or request, please contact me.
# Kazuhiro Masuyama - Associate Systems Engineer - East Japan Systems Engineering 2
# kmasuyam@cisco.com
# 2017/03/09

import CMX_Cloud_API
import CMX_API


"""
x = CMX_API.Location("learning","learning")
x.clients_history()


a = CMX_Cloud_API.Connect("admin@cisco.com","cisco")
param = {"start":"2017-02-17T10:00::00Z",
         "end":"2017-02-18T17:00::00Z",
         "index":"10",
         "count":"100",
         "status":"active",
         "authtype":"social",
         "mac":"00:11:22:33:44:55:66",
         "device":"smartphone",
         "os":"Android5.1",
         "language":"Japanese",
         "all":"question"
         }
a.query_user_sessions()




params = {"granularity":"daily","period":"this month","yAxis":"absoluteDevices","timeRange":"10:00-12:00","aggregate":"none","areas":["param1","param2"],"includeStationary":"false","connectionState":"all","expandAll":"true"}
b = CMX_API.Analytics("learning","learning")
b.manufacturer_breakdown(params)
"""
params = {
	"campusname": "CiscoCampus",
	"buildingname": "Building 9",
	"floorname": "IDEAS!"
}

x = CMX_API.Configuration("https://msesandbox.cisco.com:8081","learning","learning")
x.floor_image(params)