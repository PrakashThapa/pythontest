Documentation :
===============


part 1 :
========
Simple download the image: 
```
    python PsdFileStore.py  -f sample.txt -d data
 ```

options:
* -f or --file : file that contains URLs default
* -d or --dir : directory to store the the downloaded file, default: data
*  -h or --help : for help

part 2 :
========

For every 5 minutes script execution, cronjob can be used even though there are alternatives. `cron.sh` contains the script which can be executed with crontab like: 

``` 
    */5 * * * * /PATH_TO_FILE/cron.sh 
```

To serve Downloaded images via http, we need a http server  that can server http request. For example, the ` server.py` provide http service and the files can be found in like http://127.0.0.1:7001/data/ when server.py script run:
```
python server.py 
```

