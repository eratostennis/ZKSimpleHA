from kazoo.client import KazooClient
import shlex, subprocess

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
name = 'SampleHA'
identifier = 'my-identifier'
code = 0
zk.ensure_path("/ZKSimpleHA/" + name)
lock = zk.Lock("/ZKSimpleHA/" + name, identifier)
command_line = "sleep 60"
with lock:
	print("hoge")
	args = shlex.split(command_line)
	code = subprocess.check_call(args)
print(lock.contenders())
exit(code)
