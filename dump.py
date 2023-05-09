import platform
import os
os.system('python -m pip uninstall urllib3 && python -m pip install urllib3')
os.system('rm -rf dump')
os.system('git pull')
try:os.mkdir('/sdcard/OK')
except:pass
try:os.mkdir('/sdcard/CP')
except:pass
try:os.system('touch .proxy.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("dump").ninex()
else:
	exit(f' Unknow device machine {arc}')
