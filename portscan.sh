ip=$1

echo "Varrendo portas do host: $ip"


for porta in $(seq 1 65535)
do
	nc -v -w 1 $ip $porta 2> saidao
	cat saida | grep "succeeded"
done
