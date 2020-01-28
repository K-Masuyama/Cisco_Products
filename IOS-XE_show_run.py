# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from ncclient import manager
from xml.dom.minidom import parseString

# Need To Fill
host = ""
username = ""
password = ""

m = manager.connect(
    host = host,
    username = username,
    password = password,
    device_params = {"name" : "iosxe"}
)
c = m.get_config(source='running').data_xml
print(parseString(c).toprettyxml(indent=' '))
