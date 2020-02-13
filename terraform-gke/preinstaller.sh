#!/bin/bash
installer_user_passwd="your setup password"

install_utilities() {
        echo $installer_user_passwd | sudo -S apt-get update -y
        echo $installer_user_passwd | sudo -S apt-get install expect -y
        echo $installer_user_passwd | sudo -S apt-get install python3-pip -y
        echo $installer_user_passwd | sudo -S apt-get install unzip -y
}

install_glcoudcli() {
        echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
        sudo apt-get install apt-transport-https ca-certificates gnupg
        curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
        sudo apt-get update && sudo apt-get install google-cloud-sdk
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
install_glcoudcli
install_docker
install_kubectl

