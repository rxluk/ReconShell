url="$1"

domains=$(wget -q -O - "$url" | grep -Eo "https?://[^\"]+" | cut -d "/" -f 3 | sort -u)

result=""

for domain in $domains; do

	ip=$(host "$domain" | grep "has address" | head -n 1 | cut -d " " -f 4)

	if [ "$ip" = "" ]; then
		ip="N/A"
	fi

	echo -e "$ip $domain"
done
