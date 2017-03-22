root@Gargoyle:~# cat update-hosts.sh
#!/bin/sh
>/etc/dnsmasq.conf
>/etc/dnshosts.conf
wget https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt -O /etc/dnshosts.conf
wget https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt -O /etc/dnsmasq.conf
wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/openwrt/win10/extra/dnsmasq.conf -O - >> /etc/dnsmasq.conf
wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/openwrt/win10/update/dnsmasq.conf -O - >> /etc/dnsmasq.conf
wget https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/openwrt/win10/spy/dnsmasq.conf -O - >> /etc/dnsmasq.conf

sed -i '/whitelist/d' /etc/dnsmasq.conf

/etc/init.d/dnsmasq stop
/etc/init.d/dnsmasq start
