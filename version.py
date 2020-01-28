# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from ncclient import manager
from xml.dom.minidom import parseString

host = "10.71.134.99"
username = "admin"
password = "Cisco123"

m = manager.connect(
    host = host,
    username = username,
    password = password,
    device_params = {"name" : "iosxe"}
)
payload = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <version/>
    </native>
</filter>
"""
c = m.get(payload).data_xml
print(parseString(c).getElementsByTagName('version')[0].firstChild.data)
