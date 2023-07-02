import ncclient

with ncclient.manager.connect(
host='192.168.1.1',
port=830,username='root',
password='test398101469!',
allow_agent=False) as m:
print(m.get_config('running').data_xml)
