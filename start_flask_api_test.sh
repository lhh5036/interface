#/bin/bash
pid=$(ps x | grep "gunicorn_config.py" |  grep -v grep | awk '{print $1}')
echo $pid
kill -9 $pid
nohup /usr/local/python3/bin/gunicorn -c gunicorn_config.py manage:app > log.out 2>&1 &
tail -n 10 /home/InterfaceAutoTest/log.out
