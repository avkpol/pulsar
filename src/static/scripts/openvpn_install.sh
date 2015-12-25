#!/bin/bash
# Author : Bello Hostelman
# 081211 EDD : added openssl install 
# 081211 EDD : automated testerSSLTSL : tester les nÃ©gociations SSL/TSL et initialisation du SSL
# 081211 EDD : add cd /etc/openvpn/easy-rsa at serveral locations before execution of /etc/openvpn/easy-rsa/vars

function installOpenVPN(){
 #installation du openvpn
 apt-get install -y --allow-unauthenticated openvpn
 apt-get install -y --allow-unauthenticated openssl
 apt-get install -y --allow-unauthenticated libssl-dev
 # brew install openvpn # installing for mac

 #copie du dossier exemple ver /etc/openvpn
 mkdir /etc/openvpn
 cp -R /usr/share/doc/openvpn/examples/* $WORKDIR
 mkdir /etc/openvpn/easy-rsa/keys
 return 0
}

function testerSSLTSL(){
 #test SSL/TSL nÃ©gociantions 
 echo -e "Vous souhaitez tester les nÃ©gociation SSL/TSL\r"
 echo -e "veuilez lancer lancer les deux commandes \r" 
 echo -e "ci-dessous dans deux shell difÃ©rents et simultanÃ©ment\r\n"
 echo -e "sur chaque shell\r"
 echo -e " 1 - cd /etc/openvpn/\r"
 echo -e " 2 - openvpn --config $WORKDIR/sample-config-files/loopback-server"
 echo -e " 3 - openvpn --config $WORKDIR/sample-config-files/loopback-client"
 
 cd /etc/openvpn/

 openvpn --config $WORKDIR/sample-config-files/loopback-server &
 openvpn --config $WORKDIR/sample-config-files/loopback-client &

 return 0
}

function testerCrypto(){
 openvpn --genkey --secret key
 openvpn --test-crypto --secret key
 return 0
}

function getClientConf(){
 cd /$WORKDIR
 wget $FILEURL/client.conf
 return 0
}

function getServerConf(){
 cd /$WORKDIR
 wget $FILEURL/server.conf
 return 0
}

function getVarsFile(){
 #chargement des varibles dans l'environement
 cd /etc/openvpn/easy-rsa
 mv $WORKDIR/easy-rsa/vars $WORKDIR/easy-rsa/vars.org
 cd $WORKDIR/easy-rsa/
 wget $FILEURL/vars
 return 0
}

function genSecretKey(){
 # charger les varibles dans l'environement shell
 cd /etc/openvpn/easy-rsa
 source $WORKDIR/easy-rsa/vars
 #

 $WORKDIR/easy-rsa/clean-all
 $WORKDIR/easy-rsa/build-ca

 #gÃ©nÃ©ration des clÃ©s
 $WORKDIR/easy-rsa/build-key server
 $WORKDIR/easy-rsa/build-dh

 getServerConf

 return 0
}

function genOneSecretKey(){
 echo "Veuillez entrer le nom de la cle : "
 read keyname
 cd /etc/openvpn/easy-rsa
 source $WORKDIR/easy-rsa/vars
 #generation des cles
 $WORKDIR/easy-rsa/build-key $keyname
 $WORKDIR/easy-rsa/build-dh

 return 0
}

function menuOpenVPNserver(){
 echo -e "Bienvenu a  l'installation Pulsar VPN\r\n"
 echo -e "[1] installation vpn\r"
 echo -e "[2] tester crypto\r"
 echo -e "[3] tester les nÃ©gociations SSL/TSL\r"
 echo -e "[4] gÃ©nÃ©ration de clÃ©s cas installation serveur\r"
 echo -e "[5] obtenir server.conf\r"
 echo -e "[7] lanser le server\r"
 echo -e "[10] gÃ©nÃ©rer une clÃ©"
 echo -e "[0] quiter\r"
 return 0
}

function menuOpenVPNClient(){
 echo -e "Bienvenu Ã  l\\'installation Pulsar VPN\r\n"
 echo -e "[1] installation vpn\r"
 echo -e "[6] obtenir client.conf\r"
 echo -e "[8] copier la clÃ©\r"
 echo -e "[9] lancer le client\r"
 echo -e "[0] quiter\r"
 return 0
}


function startServer(){
 openvpn $WORKDIR/server.conf &
 return 0
}

function startClient(){
 openvpn $WORKDIR/client.conf &
 return 0
}

function cpKeyToClient(){
 echo "Veuillez entrer le nom de la clÃ© :" 
 read key
 
 echo "Veuillez entrer l'adresse ip du serveur :" 
 read ip 
 
 scp root@$ip:$WORKDIR/easy-rsa/keys/$key* $WORKDIR/easy-rsa/keys
 
 echo "Souhaitez-vous également le fichier ca.crt [y/n] : "
 read answer
 if [ "$answer"="y" ] ; then
  scp root@$ip:$WORKDIR/easy-rsa/keys/ca.crt $WORKDIR/easy-rsa/keys
 fi
 
 return 0
}

#TODO conbiner ce script avec le fichier functions_utiles

choix=10
export WORKDIR="/etc/openvpn"
export FILEURL="http://scripts/etch/testing/files/openvpn"
ls $WORKDIR >> /dev/null || mkdir $WORKDIR


while [ "$choix" != "0" ]
do
 #affichage du meu et lecture du choix
 echo -e "\n"
 if [ "$1" = "client" ] ; then
  menuOpenVPNClient
 elif [ "$1" = "server" ] ; then
  menuOpenVPNserver
 elif [ "$1" = "default" ] ; then
  installOpenVPN
  getVarsFile
  getServerConf
  getClientConf
  exit 0
 else
  echo -e "Indiquer le type d'installation (client/server/default)\n"
  exit 0
 fi 
 read choix

 case $choix in
  "1") 
   installOpenVPN
  ;;
  "2") 
   testerCrypto
  ;;
  "3") 
   testerSSLTSL
  ;;
  "4") 
   #getVarsFile
   genSecretKey
  ;;
  "4") 
   genSecretKey
  ;;
  "5") 
   getServerConf
  ;;
  "6") 
   getClientConf
  ;;
  "7") 
   startServer
  ;;
  "8") 
   cpKeyToClient
  ;;
  "9") 
   startClient
  ;;
  "10") 
   genOneSecretKey
  ;;
  "0") 
   exit 0
  ;;
  *) 
   echo "command not found"
  ;;
  esac
done
  echo -e "[10] gÃ©nÃ©rer une clÃ©"
