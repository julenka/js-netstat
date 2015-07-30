from subprocess import Popen, PIPE
import re
import datetime

command = "bin/js-netstat"
p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = p.communicate(None)


pattern = re.compile(r"^.*obytes (\d+)\n$")
m = pattern.match(stdout)

print "{},{}".format(datetime.datetime.now(), m.groups()[0])


