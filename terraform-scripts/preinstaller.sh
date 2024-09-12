#!/bin/bash
installer_user_passwd="your setup password"

install_utilities() {
	echo $installer_user_passwd | sudo -S apt-get update -y
	echo $installer_user_passwd | sudo -S apt-get install expect -y	
	echo $installer_user_passwd | sudo -S apt-get install python3-pip -y
	echo $installer_user_passwd | sudo -S apt-get install unzip -y
	echo $installer_user_passwd | sudo -S apt install crudini -y
}

install_awscli() {
	echo $installer_user_passwd | sudo -S  apt-get  install awscli -y
	sudo pip3 install --upgrade --user awscli
	aws --version
	if [[ "${?}" -ne 0 ]];then
		echo "awscli note installed properly ..."
		exit 0
	fi
}

install_iam_authenticator() {
	curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator
	curl -o aws-iam-authenticator.sha256 https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator.sha256
	openssl sha1 -sha256 aws-iam-authenticator
	chmod +x ./aws-iam-authenticator
	mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$HOME/bin:$PATH
	sudo cp ./aws-iam-authenticator /usr/local/bin
	echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
	chmod a+x ~/.bashrc
	source ~/.bashrc
	sleep 10s
	aws-iam-authenticator help
        if [[ "${?}" -ne 0 ]];then
                echo "awscli note installed properly ..."
                exit 0
        fi
}

install_docker() {
	command -v docker
	if [[ "${?}" -ne 0 ]];then
		VERSIONSTRING="5:18.09.2~3-0~ubuntu-bionic"
		echo "Docker does not exist\n"
		echo "installing Docker\n"
		sudo apt-get remove docker docker-engine docker.io containerd runc
		sudo apt-get -y update
		sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
		curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
		sudo apt-key fingerprint 0EBFCD88
		sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
		sudo apt-get -y update
		sudo apt-get install -y docker-ce=$VERSIONSTRING docker-ce-cli=$VERSIONSTRING containerd.io
	fi
}

install_kubectl() {
	command -v kubectl
	if [[ "${?}" -ne 0 ]]; then
  		echo "Kubectl does not exist\n"
  		echo "Installing kubectl\n"
  		curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
  		chmod +x ./kubectl
  		sudo mv ./kubectl /usr/local/bin/kubectl
  		kubectl version
	fi
}

install_utilities
install_awscli
install_iam_authenticator
install_docker
install_kubectl
