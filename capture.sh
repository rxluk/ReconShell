find="$1"

COLOR1="\033[32m"
COLOR2="\033[37m"
COLOR3="\033[31m"

if [ "$find" = "" ]; then
	echo -e "${COLOR3}Erro: ${COLOR2}Falta de parâmetro ${COLOR1}(URL)${COLOR2}"
	exit 1
fi
echo
echo "============================================="
echo -e "           Analisando: ${COLOR3}$find${COLOR2}"
echo "============================================="

result=$(wget -q -O - "$find" | grep -Eo "https?://[^\"]+" | cut -d "/" -f 3 | sort -u)

if [ "$result" = "" ]; then
	echo "Nenhum resultado encontrado."
else
	echo "=                 Resultado                 ="
	echo "============================================="
	echo

	for line in $result; do

		ip=$(host "$line" | grep "has address" | head -n 1 | cut -d " " -f 4)

		if [ "$ip" = "" ]; then
			ip="N/A"
		fi

		if [ $((i % 2)) -eq 0 ]; then
			echo -e "${COLOR3}$ip\t${COLOR2}$line"
		else
			echo -e "${COLOR3}$ip\t${COLOR1}$line"

		fi
		i=$((i + 1))
	done
	echo
fi

