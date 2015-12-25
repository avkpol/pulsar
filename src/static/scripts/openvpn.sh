#!/bin/bash
# Author : Bello Hostelman
# 081211 EDD : added openssl install 
# 081211 EDD : automated testerSSLTSL : tester les négociations SSL/TSL et initialisation du SSL
# 081211 EDD : add cd /etc/openvpn/easy-rsa at serveral locations before execution of /etc/openvpn/easy-rsa/vars

export SCRIPT=openvpn
export distribution=wheezy
export FILEURL=http://scripts/${distribution}/files/${SCRIPT}
export WORKDIR="/etc/openvpn"
#export WORKDIR=/var/scripts/
export LOGDIR=/var/log/scripts
export LOGFILE=$LOGDIR/${SCRIPT}.log
export ERRORFILE=$LOGDIR/${SCRIPT}.errors
export OPENSSL="/usr/bin/openssl"
ls $WORKDIR >> /dev/null || mkdir $WORKDIR

apt-get install -y psmisc #for killall

#function installOpenVPN(){
 #installation du openvpn
 apt-get install -y --allow-unauthenticated openvpn
 #apt-get install -y --allow-unauthenticated openssl # openssl already installed with openvpn
 #apt-get install -y --allow-unauthenticated libssl-dev # libssl-dev already installed with openvpn

 #copie du dossier exemple ver /etc/openvpn
 #mkdir /etc/openvpn # already created in line 16: ls $WORKDIR >> /dev/null || mkdir $WORKDIR
 cp -R /usr/share/doc/openvpn/examples/* $WORKDIR
 mkdir /etc/openvpn/easy-rsa/keys

 # add index.txt.attr
 cd /etc/openvpn/easy-rsa/keys/
 mv index.txt.attr index.txt.attr.old
 wget $FILEURL/index.txt.attr
 
 cd /etc/openvpn/

#function testerCrypto(){
 openvpn --genkey --secret key
 openvpn --test-crypto --secret key

 killall openvpn

#function getVarsFile(){
 #chargement des varibles dans l'environement
 cd $WORKDIR/easy-rsa/
 cp $WORKDIR/easy-rsa/1.0/* .
 mv $WORKDIR/easy-rsa/vars $WORKDIR/easy-rsa/vars.org
 cd $WORKDIR/easy-rsa/
 wget $FILEURL/vars
# return 0
#}

#function genSecretKey(){
 # charger les varibles dans l'environement shell
 cd /etc/openvpn/easy-rsa
 source $WORKDIR/easy-rsa/vars
 #

 $WORKDIR/easy-rsa/clean-all
# echo -e \\n\\n\\n\\n\\n\\n\\n | $WORKDIR/easy-rsa/build-ca

 #génération des clés
# echo -e \\n\\n\\n\\n\\n$(hostname)\\n\\n\\n\\ny\\ny\\n >9CR
# echo -e \\n\\n\\n\\n\\n$(hostname)\\n\\n\\n\\n\\ny\\ny\\n | $WORKDIR/easy-rsa/build-key server
# $WORKDIR/easy-rsa/build-key server < 9CR
# $WORKDIR/easy-rsa/build-key server
# $WORKDIR/easy-rsa/build-dh

# openvpn --config $WORKDIR/sample-config-files/loopback-server &
# openvpn --config $WORKDIR/sample-config-files/loopback-client &



 cd $WORKDIR
 wget $FILEURL/server.conf

 cd /var/scripts
 mv openvpn_client openvpn_client.operations
 wget $FILEURL/openvpn_client 
 wget $FILEURL/openvpn_menu 

 chmod +x openvpn_client
 chmod +x openvpn_menu

 openvpn $WORKDIR/server.conf &

exit