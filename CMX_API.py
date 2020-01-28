# -*- coding: utf-8 -*-

# This script is for running On-Premiss CMX API. 
# "Class" is written to fit in each API method. (Please refer to https://msesandbox.cisco.com:8081/apidocs/)
# In addition, each method within classes corresponds to APIs written in above web page.
# If you have question or request, please contact me.
# Kazuhiro Masuyama - Associate Systems Engineer - East Japan Systems Engineering 2
# kmasuyam@cisco.com
# 2017/03/09


import requests
requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth
import json
import base64
from PIL import Image
from StringIO import StringIO



class Analytics:
	def __init__(self,url,username,password):
		self.username = username
		self.password = password
		self.url_base = url + "/api/analytics/v1/%s"

	def get_method(self,url):
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def post_method(self,url,params=None):
		header = {"Content-Type":"application/json"}
		try:
			request = requests.post(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				headers = header,
				data = json.dumps(params)
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def analytics_summary(self):
		url = self.url_base % "summary"
		self.get_method(url)

	def now_client_count_get(self):
		url = self.url_base % "now/clientCount"
		self.get_method(url)

	def now_connected_detected_get(self):
		url = self.url_base % "now/connectedDetected"
		self.get_method(url)

	def analytics_notification_alerts(self,params): # params は Key が elementid, timeframe のディクショナリ
		if params["elementid"]:
			elementid = "/" + str(params["elementid"])
		else:
			elementid = ""

		if params["timeframe"]:
			timeframe = "/" + str(params["timeframe"])
		else:
			timeframe = ""

		url = self.url_base % "notifications/deviceCount" + elementid + timeframe
		self.get_method(url)

		# Analytics Social Media Analytics API は 2017/2/3 時点で Resource Not Found

	def path(self,params):
		url = self.url_base % "path"
		self.post_method(url,params)

	def queue_times(self,params):
		url = self.url_base % "queue"
		self.post_method(url,params)

	def device_count(self,params):
		url = self.url_base % "deviceCount"
		self.post_method(url,params)

	def network_state(self,params):
		url = self.url_base % "connectedDetected"
		self.post_method(url,params)

	def manufacturer_breakdown(self,params):
		url = self.url_base % "manufacturers"
		self.post_method(url,params)

	def dwelltime(self,params):
		url = self.url_base % "deviceDwell"
		self.post_method(url,params)

	def now_client_count_post(self,params):
		url = "now/clientCount"
		self.post_method(url,params)

	def now_connected_detected_post(self,params):
		url = self.url_base % "now/connectedDetected"
		self.post_method(url,params)

	def dwell_breakdown(self,params):
		url = self.url_base % "dwellBreakdown"
		self.post_method(url,params)

	def overview(self,params):
		url = self.url_base % "overview"
		self.post_method(url,params)



class Location:
	def __init__(self,url,username,password):
		self.username = username
		self.password = password
		self.url_base = url + "/api/location/%(first)s/%(second)s"

	def get_method(self,url,params=None):
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				params = params)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def post_method(self,url,params=None):
		header = {"Content-Type":"application/json"}
		try:
			request = requests.post(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				headers = header,
				data = json.dumps(params)
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def tags_information_count(self):
		url_dic = {"first":"v1","second":"tags/count"}
		url = self.url_base % url_dic
		self.get_method(url)

	def tags_information(self):
		url_dic = {"first":"v1","second":"tags"}
		url = self.url_base % url_dic
		self.get_method(url)

	def tags_information_by_macaddress(self,macaddress):
		url_dic = {"first":"v1","second":"tags/%s" % macaddress}
		url = self.url_base % url_dic
		self.get_method(url)

	def clients_history_unique_clients(self,params):
		url_dic = {"first":"v1","second":"history/uniqueclientsbyhierarchy"}
		url = self.url_base % url_dic
		self.get_method(url,params)

	def clients_history_by_ipaddress(self,params):
		url_dic = {"first":"v1","second":"historylite/byipaddress/%s" % params["ipv4address"]}
		url = self.url_base % url_dic
		self.get_method(url,{"date":params["date"]})

	def clients_history_by_username(self,params):
		url_dic = {"first":"v1","second":"historylite/byusername/%s" % params["username"]}
		url = self.url_base % url_dic
		self.get_method(url,{"date":params["date"]})

	def clients_history_by_macaddress_and_date(self,params):
		url_dic = {"first":"v1","second":"historylite/clients/%s" % params["macaddress"]}
		url = self.url_base % url_dic
		self.get_method(url,{"date":params["date"]})

	def clients_history_by_macaddress(self,macaddress):
		url_dic = {"first":"v1","second":"historylite/clients/%s" % macaddress}
		url = self.url_base % url_dic
		self.get_method(url)

	def clients_history(self):
		url_dic = {"first":"v1","second":"clients"}
		url = self.url_base % url_dic
		self.get_method(url)

	def beacon_management_count(self):
		url_dic = {"first":"v1","second":"beacon/count"}
		url = self.url_base % url_dic
		self.get_method(url)

	def beacon_management(self):
		url_dic = {"first":"v1","second":"beacon"}
		url = self.url_base % url_dic
		self.get_method(url)

	def beacon_management_by_macaddress(self,macaddress):
		url_dic = {"first":"v1","second":"beacon/%s" % macaddress}
		url = self.url_base % url_dic
		self.get_method(url)

	def beacon_management_by_floorrefid(self,floorrefid):
		url_dic = {"first":"v1","second":"beacon/floor/%s" % floorrefid}
		url = self.url_base % url_dic
		self.get_method(url)

	def beacon_management_search(self,params):# params の key は floorid, macaddress, name, uuid, major, minor
		filterstring = ""
		url_dic_2 = {}
		url_dic = {"first":"v1","second":"beacon/search/%(floorrefid)s/%(filterstring)s"}
		if params["macaddress"]:
			filterstring += "mac=%s " % params["macaddress"]
		else:
			pass

		if params["name"]:
			filterstring += "name=%s " % params["name"]
		else:
			pass

		if params["uuid"]:
			filterstring += "uuid=%s " % params["uuid"]
		else:
			pass

		if params["major"]:
			filterstring += "major=%s " % params["major"]
		else:
			pass

		if params["minor"]:
			filterstring += "minor=%s" % params["minor"]
		else:
			pass

		if filterstring[len(string)-1] == " ":
			filterstring = filterstring.rstrip()

		url_dic_2["floorrefid"] = params["floorrefid"]
		url_dic_2["filterstring"] = filterstring

		url = self.url_base % url_dic % url_dic_2
		self.get_method(url)

	def beacon_management_info(self,floorrefid):
		url_dic = {"first":"v1","second":"beacon/info/%s" % floorrefid}
		url = self.url_base % url_dic
		self.get_method(url)

	def northbound_notification_types_and_attributes(self):
		url_dic = {"first":"v1","second":"attributes"}
		url = self.url_base % url_dic
		self.get_method(url)

	def active_clients_count(self):
		url_dic = {"first":"v2","second":"clients/count"}
		url = self.url_base % url_dic
		self.get_method(url)

	def active_clients(self,params=None):# params はディクショナリで type と parameter がKey
	                                     # type が search の場合、parameter の value はリストで 0 が ipAdress, macAddress, username のいずれかで 1 がその値
	                                     # type が sort の場合、parameter の value はリストで 0 が lastLocatedTime, userName, macAddress, ssId, dot11status で 1 がその値
		url_dic = {"first":"v2","second":"clients"}
		url_beta = self.url_base % url_dic
		if params["type"] == "search":
			url = url_beta + "?" + params["parameter"][0] + "=" + params["parameter"][1]
		elif params["type"] == "sort":
			url = url_beta + "?" + "sortBy=" + params["parameter"][0] + ":" + params["parameter"][1]

		self.get_method(url)

	def runs_location_compliance_tests_get(self,params):# params の key は macaddress, floorid
		url_dic = {"first":"v1","second":"compliance/clientcompliance/rules/mac/%(macaddress)s/%(floorid)s"}
		url = self.url_base % url_dic % params
		self.get_method(url)

	def runs_location_compliance_tests_floor_hierarchy(self,macaddress):
		url_dic = {"first":"v1","second":"compliance/clientcompliance/floor/%s" % macaddress}
		url = self.url_base % url_dic
		self.get_method(url)

	def runs_location_compliance_tests_post(self,ruleid):
		url_dic = {"first":"v1","second":"compliance/clientcompliance/remediate/%s" % ruleid}
		url = self.url_base % url_dic
		self.post_method(url)

	def runs_location_compliance_tests(self,params):
		url_dic = {"first":"v1","second":"compliance/client/run"}
		url = self.url_base % url_dic
		self.post_method(url,params)



class Configuration:
	def __init__(self,url,username,password):
		self.username = username
		self.password = password
		self.url_base = url + "/api/configuration/v1/%s"
		self.url_base_2 = url + "/api/config/v1/%s"

	def get_method(self,url,params=None):
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				params = params)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def post_method(self,url,params=None):
		header = {"Content-Type":"application/json"}
		try:
			request = requests.post(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				headers = header,
				data = json.dumps(params)
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def put_method(self,url,params=None):
		try:
			request = requests.put(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				data = json.dumps(params)
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def delete_method(self,url,params=None):
		try:
			request = requests.delete(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				params = params)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def northbound_notification_types_and_attributes(self):
		url = self.url_base % "attributes"
		self.get_method(url)

	def history_alerts(self,params):
		url = self.url_base_2 % "history/alerts"
		self.get_method(url,params)

	def all_notification_subscription(self):
		url = self.url_base_2 % "notifications"
		self.get_method(url)

	def notification_by_name(self,name):
		path = "notifications/" + name
		url = self.url_base_2 % path
		self.get_method(url)

	def notification_subscription_exist_check(self,name):
		path = "notifications/exists/" + name
		url = self.url_base_2 % path
		self.get_method(url)

	def system_alert_subscription(self):
		url = url_base_2 % "notification/alerts"
		self.get_method(url)

	def all_sites(self):
		url = url_base_2 % "sites"
		self.get_method(url)

	def site_by_name_or_id(self,name_or_id):
		path = "sites/" + name_or_id
		url = url_base_2 % path
		self.get_method(url)

	def all_users(self):
		url = url_base_2 % "aaa/users"
		self.get_method(url)

	def all_roles(self):
		url = url_base_2 % "aaa/roles"
		self.get_method(url)

	def user_by_username(self,username):
		path = "aaa/users/" + username
		url = url_base_2 % path
		self.get_method(url)

	def version_CMX(self):
		url = url_base_2 % "version/image"
		self.get_method(url)

	def retrieve_system_settings(self,params):#params は key が component, key のディクショナリ
		path = "system/preferences/%(component)s/%(key)s" % params
		url = url_base_2 % path
		self.get_method(url)

	def alerts_count(self):
		url = url_base_2 % "alerts/count"
		self.get_method(url)

	def all_alerts(self):
		url = url_base_2 % "alerts"
		self.get_method(url)

	def optout_devices_within_range(self,params):# params は key が validFrom, validTo のディクショナリで、value は "yyyy-mm-dd HH:mm:ss" の形
		url = url_base % "optout/devices"
		self.get_method(url,params)

	def optout_devices_count(url):
		url = url_base % "optout/count"
		self.get_method(url)

	def all_map_elements_count(self):
		url = url_base_2 % "maps/count"
		self.get_method(url)

	def all_building_name(self):
		url = url_base_2 % "maps/building/list"
		self.get_method(url)

	def all_building_name_by_campus_name(self,name):
		path = "maps/building/list/" + name
		url = url_base_2 % path
		self.get_method(url)

	def all_floor_name(self):
		url = url_base_2 % "maps/floor/list"
		self.get_method(url)

	def all_floor_name_by_building_name(self,name):
		path = "maps/floor/list" + name
		url = url_base_2 % path
		self.get_method(url)

	def all_maps(self):
		url = url_base_2 % "maps"
		self.get_method(url)

	def campus_by_name(self,name):
		path = "maps/info/" + name
		url = url_base_2 % path
		self.get_method(url)

	def building_by_name(self,params):# params は、key が campusName, buildingName のディクショナリ
		path = "maps/info/%(campusName)s/%(buildingName)s" % params
		url = url_base_2 % path
		self.get_method(url)

	def floor_by_name(self,params):
		path = "maps/info/%(campusName)s/%(buildingName)s/%(floorName)s"
		url = url_base_2 % path
		self.get_method(url)

	def floor_image(self,params):
		path = "maps/image/%(campusname)s/%(buildingname)s/%(floorname)s" % params
		url = self.url_base_2 % path
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				i = Image.open(StringIO(request.content))
				i.show()
		except requests.exceptions.RequestException as e:
			print(e)

	def floor_image_by_image_name(self,image_name):
		path = "maps/imagesource/" + image_name
		url = self.url_base_2 % path
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				)
			if request.content == "CMX Error":
				print(request.content)
			else:
				i = Image.open(StringIO(request.content))
				i.show()
		except requests.exceptions.RequestException as e:
			print(e)


	# 残りの POST, PUT, DELETE API
	# 動くなら



class Connect:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.url = url + "/api/connect/v1/clients"

	def get_method(self,url,params):
		try:
			request = requests.get(
				url = url,
				auth = HTTPBasicAuth(self.username,self.password),
				verify = False,
				params = params)
			if request.content == "CMX Error":
				print(request.content)
			else:
				parsed = json.loads(request.content)
				print(json.dumps(parsed, indent=2))

		except requests.exceptions.RequestException as e:
			print(e)

	def query_user_sessions(self,params):
		self.get_method(self.url,params)