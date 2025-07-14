for domain in $(cat dominios)
do
	host $domain | grep -v "not found" 
done
