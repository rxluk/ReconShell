#!/bin/bash

if [ -z "$1" ]; then
    echo "Uso: $0 <URL>"
    exit 1
fi

url="$1"
base_domain=$(echo "$url" | cut -d '/' -f 3)
base_url_for_test=$(echo "$url" | cut -d '?' -f 1 | sed 's/\/$//')

html_content=$(wget -q -O - "$url")

test_endpoint() {
    local path_to_test="$1"
    local full_url_for_test=""

    local protocol="http"
    if [[ "$url" =~ ^https:// ]]; then
        protocol="https"
    fi

    if [[ "$path_to_test" =~ ^https?:// ]]; then
        full_url_for_test="$path_to_test"
    elif [[ "$path_to_test" =~ ^// ]]; then
        full_url_for_test="$protocol:$path_to_test"
    else
        full_url_for_test="$base_url_for_test$path_to_test"
    fi

    local methods=("GET" "POST" "PUT" "DELETE" "PATCH")
    local accepted_methods=""

    for method in "${methods[@]}"; do
        local http_code=$(curl -s -L -o /dev/null -w "%{http_code}" -X "$method" "$full_url_for_test" 2>/dev/null)

        if [[ "$http_code" != "405" ]] && [[ "$http_code" != "404" ]] && [[ "$http_code" != "000" ]]; then
            accepted_methods+="$method($http_code) "
        fi
    done
    echo "$accepted_methods"
}

echo "$html_content" | \
grep -Eo "<form[^>]*action=\"[^\"]*\"" | \
grep -Eo "action=\"[^\"]*\"" | \
cut -d '"' -f 2 | \
grep -Ev "\.(jpeg|jpg|png|gif|css|js|woff|ttf|svg|ico|pdf|webp|xml)(\?.*)?$" | while read path; do
    if [ -z "$path" ]; then continue; fi

    if [[ "$path" =~ ^https?:// ]]; then
        current_domain=$(echo "$path" | cut -d '/' -f 3)
        if [ "$current_domain" = "$base_domain" ]; then
            endpoint_path="/$(echo "$path" | cut -d '/' -f 4-)"
            methods=$(test_endpoint "$endpoint_path")
            echo -e "$endpoint_path\t$methods"
        fi
    else
        if [[ ! "$path" =~ ^/ ]]; then
            endpoint_path="/$path"
        else
            endpoint_path="$path"
        fi
        methods=$(test_endpoint "$endpoint_path")
        echo -e "$endpoint_path\t$methods"
    fi
done

echo "$html_content" | \
grep -Eo "(href|src)=\"?[^\"'> ]+\"?" | \
grep -Eo "https?://[^\"]+/[^\"']+|/[^\"']+" | \
grep -Ev "\.(jpeg|jpg|png|gif|css|js|woff|ttf|svg|ico|pdf|webp|xml)(\?.*)?$" | \
sort -u | while read path; do
    path=$(echo "$path" | tr -d '"')
    if [ -z "$path" ]; then continue; fi

    if [[ "$path" =~ ^https?:// ]]; then
        current_domain=$(echo "$path" | cut -d '/' -f 3)
        if [ "$current_domain" = "$base_domain" ]; then
            endpoint_path="/$(echo "$path" | cut -d '/' -f 4-)"
            methods=$(test_endpoint "$endpoint_path")
            echo -e "$endpoint_path\t$methods"
        fi
    else
        if [[ ! "$path" =~ ^/ ]]; then
            endpoint_path="/$path"
        else
            endpoint_path="$path"
        fi
        methods=$(test_endpoint "$endpoint_path")
        echo -e "$endpoint_path\t$methods"
    fi
done
