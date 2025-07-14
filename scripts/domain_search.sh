url="$1"

domains=$(wget -q -O - "$url" | grep -Eo "https?://[^\"]+" | cut -d "/" -f 3 | sort -u)

result=""

for domain in $domains; do

	echo "$domain" | grep "@" > /dev/null && continue
	echo "$domain" | grep "^localhost" > /dev/null && continue
	echo "$domain" | grep "^0\." > /dev/null && continue

	ip=$(host "$domain" 2>/dev/null | grep "has address" | head -n 1 | cut -d " " -f 4)

	if [ "$ip" = "" ]; then
		continue
	fi

	echo -e "$ip $domain"
done
