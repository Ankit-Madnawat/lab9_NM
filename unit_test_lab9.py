import unittest
from netmiko import ConnectHandler
from netman_netconf_obj2 import config


class TestConfig(unittest.TestCase):
    def test_loopback(self):
        table = config()
        loopbackip = []
        for row in table:
            row.border = False
            row.header = False
            loopbackip.append(row.get_string(fields=["Loopback 99 IP"]).strip())
        self.assertEqual(loopbackip[2], '10.1.3.1/24')

    def test_area(self):
        table = config()
        ospf_area = []
        for row in table:
            row.border = False
            row.header = False
            ospf_area.append(row.get_string(fields=["Loopback 99 IP"]).strip())
        self.assertEqual(ospf_area[0], 0)
    

    def test_ping(self):
        device = {
            'device_type': 'cisco_ios',
            'host': '198.51.100.12',
            'username': 'lab',
            'password': 'lab123'
        }
        connection = ConnectHandler(**device)
        ping = connection.send_command("ping 10.1.5.1 source 10.1.2.1")
        connection.disconnect()
        self.assertEqual(type(ping), True)

if __name__ == '__main__':
    unittest.main()
