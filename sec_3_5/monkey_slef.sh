#########################################################################
# File Name: monkey_slef.sh
# Author: lw3968
# mail: cainiao367@163.com
# Created Time: 2016年01月06日 星期三 14时39分41秒
#########################################################################
#!/bin/bash
_cnt=1
#adb shell input keyevent 26
echo "Monkey begin $_cnt"
while true;
do
sleep 3
echo "Monkey  $_cnt times"
	_cnt=$(($_cnt + 1))
#adb shell "monkey -v-v --ignore-crashes --ignore-timeouts --kill-process-after-error --ignore-security-exceptions --throttlei 1000 -v 20000000" 
adb shell "monkey -v-v --pct-syskeys 0 --ignore-crashes --ignore-timeouts --kill-process-after-error --ignore-security-exceptions --throttle 10 -v 1000000"
	sleep 5
	adb wait-for-devices
	sleep 15
	_cnt=$(($_cnt + 1))
done
