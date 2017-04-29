# scripts

1. update-dnsmasq-hosts.sh - automaticly update dnsmasq blocking ip list used in gargoyle router.
2. sms.py - forward sms to mailbox using smtp in gammu-smsd.
  # usage:
  # cat /etc/gammu-smsdrc | grep RunOn
  # RunOnReceive = /usr/local/bin/sms.py
