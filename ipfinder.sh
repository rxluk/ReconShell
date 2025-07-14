for i in $(seq 1 254); do
    ping -c1 -w1 192.168.104.$i | grep "64 bytes" | cut -d " " -f 4 | tr -d :
done

