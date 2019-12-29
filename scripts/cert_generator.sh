#!/bin/bash
set -e

#pass file with names separated by spaces as arg 1

for value in `cat $1`; do
    echo "Setting variables for $value"
    password="$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 13 ; echo '')Aa1_"
    CN="${value}"
    O=""
    OU=""
    L="Katowice"
    ST="Slaskie"
    C="PL"
    D="CN=${CN}, OU=${OU}, O=${O}, L=${L}, ST=${ST}, C=${C}" #this is for dummy, not important
    SUBJ="/CN=${CN}/OU=${OU}/O=${O}/L=${L}/ST=${ST}/C=${C}"
    EXT="SAN=dns:${CN},dns:${value}"

    echo "Creating directory $value"
    mkdir -p ${value}
    cd ${value}

    #All of this can be done with keytool alone, in oneliner but older versions of keytool don't accept CN and dns starting with numbers, unlike openssl which doesnt give a fuck 
    echo "Generating keys"
    openssl req -x509 -nodes -newkey rsa:4096 -days 3650 -sha256 -keyout $value.key -out $value.cert -reqexts SAN -extensions SAN -subj "$SUBJ" -config <(cat /etc/pki/tls/openssl.cnf; printf "[SAN]\nsubjectAltName=DNS:$CN,DNS:$value")
    
    echo "Creating p12"
    openssl pkcs12 -export -out $value.p12 -inkey $value.key -in $value.cert -password pass:$password -name "$CN"
    
    echo "Creaing keystore"
    keytool -genkey -alias dummy -storetype JKS -keystore keystore.jks -storepass $password -keypass $password -dname "$D" #it's just easier to create jks with dummy key and delete it later...
    
    echo "Importing keys"
    keytool -v -importkeystore -alias $CN -destalias $CN -srckeystore ${value}.p12 -srcstoretype PKCS12 -destkeystore keystore.jks -deststoretype JKS -srckeypass $password -destkeypass $password -srcstorepass $password -deststorepass $password
    keytool -delete -alias dummy -keystore keystore.jks -storepass $password

    echo "Generating CSR"
    keytool -certreq -alias $CN -keyalg RSA -file $CN.csr -keystore keystore.jks -storepass $password -keypass $password

    echo "Name: $value Password: $password" > info.txt

    cd ..
done

exit 0