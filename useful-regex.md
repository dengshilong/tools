##  judge if a string is a ipv4 address
^([1-9]?[0-9]{1}|1[0-9]{2}|2[0-4][0-9]|25[0-5])(.([1-9]?[0-9]{1}|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}$

## remove html tag(from 正则指引 P305)
(?i)</?[a-z][-a-z0-9_:.]*(?=[\s>])('[^']*'|"[^"]*"|[^'">])*>
