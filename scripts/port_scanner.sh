domain="$1"
all_ports=""

for ports in $(cat ports); do
	result=$(nc -v -w 1 $domain $ports 2>&1)
	all_ports="${all_ports}\n${result}"
done

echo -e "$all_ports" | grep "succeeded" | sort -u
