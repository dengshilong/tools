from zabbix_client import ZabbixServerProxy
zapi = ZabbixServerProxy("http://10.57.17.31/")
print zapi.user.login(user="hermes", password="12345")
# print zapi.host.get({
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": ["hostid"],
#         "hostids": "10109"
#     },
#     "auth": "038e1d7b1735c6a5436ee9eae095879e",
#     "id": 1
# })
print zapi.host.get(output=['hostid', 'host'])
import time
params = {
    "name": "madfsdfsadsdfsdf",
    "active_since": 1358844540,
    # "groupids":["196"],
    "active_till": int(time.time()),
    "hostids": ["10109"],
    "timeperiods": [
        {
            "start_time": 64800,
            "period": 3600
        }
    ]
}
#print zapi.maintenance.create(**params)
params = {
    "hostids": ["10109"]
}
print zapi.maintenance.get(**params)


params = ('20',)
# print zapi.maintenance.delete('16', '17')
print zapi.maintenance.delete(*params)
