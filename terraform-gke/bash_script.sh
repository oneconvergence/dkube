#!/bin/bash -x
###########################################
#                                         #
#             DKUBE GKE SCRIPT            #
#                                         #
###########################################

#######Editable fields######
GKE_core_name=dkube-gke-demo                    #Base name of your cluster
machine_type=n1-standard-8			# Type of machine
region=us-central1                              # Region for GKE Cluster 
zone=us-central1-a				# Zone for GKE Cluster
project=dkube-public				# Specify the Project name
Node_name=gke-node				# Define Node name
max_cluster_nodes=10                            # Maximum number of managed node groups per cluster
num_cluster_nodes=2                            # Number of nodes desired for current cluster
credential_file=dkube-public-8318f4854ff1.json  # Generate Json file in Google cloud and thing should be used here
public_key=ssh-rsa.pub				# Define public key name to GKE VM
private_key=ssh-rsa				# Define private key name to access GKE VM
installer_user_passwd=user123                   #Needed only if setup requires password on sudo permission
gpu_counter=0



#######ADVANCED(When required user will modify based on setup)#######
k8s_version=1.14                                  #Kubernetes version
GKE_cluster_username=ubuntu                       #Username of the eks cluster
DISTRO=ubuntu                                     #Choose one of ubuntu/centos
DKUBEVERSION="1.4.3"                               #version of dkube to be installed
dkubeuser=ocdkube                                 #Username for dkube
dkubepass=oc123                                   #password for dkube user
#gpu_counter=0


#installer_username=`whoami`
platform=gke
#cluster_name="terraform-gke-dkube-gke-test-demo"
cluster_name="terraform-demo"
cluster_name="${cluster_name:0:9}-$GKE_core_name${cluster_name:9:14}"
echo "-------------------------------------------------------------------------------"
echo $cluster_name
#echo $installer_user_passwd | sudo -S chmod 400 $pem
echo $installer_user_passwd | sudo -S cp install $HOME

#Untar the tar file. i.e terraform script
echo $installer_user_passwd | sudo -S tar -xvf gke_script.tar
sleep 2s
echo $installer_user_passwd | sudo cp ssh-rsa ssh-rsa.pub dkube-public-8318f4854ff1.json gke-getting-started/
if [[ -e terraform_0.12.9_linux_amd64.zip ]];then
  echo $installer_user_passwd | sudo -S unzip terraform_0.12.9_linux_amd64.zip
  if [[ "${?}" -ne 0 ]];then
        echo "Something went wrong !! File terraform_0.12.9_linux_amd64.zip not unzipped."
        exit 1
  fi
  echo $installer_user_passwd | sudo -S mv terraform gke-getting-started
  if [[ "${?}" -ne 0 ]];then
        echo "Something went wrong !! Could not move file terraform into eks-getting-started directory."
        exit 1
  fi
fi

#install expect
echo $installer_user_passwd | sudo -S apt-get install expect


#Changed to working directory
echo $installer_user_passwd | sudo -S chown -R ${installer_username}:${installer_username} gke-getting-started
cd gke-getting-started

#Changed all resuorce name in terraform script

# Update provider.tf
sed -i "s/project=.*/project=\"$project\"/" provider.tf
sed -i "s/region=.*/region=\"$region\"/" provider.tf
sed -i  "s/credentials=.*/credentials=\"\$\{file(\"$credential_file\")}\"/" provider.tf

# update  variable.tf
sed -i "s/pool/$Node_name-&/g" variable.tf
sed -i  "s/1.14/$k8s_version/g" variable.tf
sed -i  "s/demo/$GKE_core_name-&/g" variable.tf
sed -i "s/us-central1-c/$zone/g" variable.tf
sed -i  "s/-1/$gpu_counter/g" variable.tf
sed -i  "s/-2/$num_cluster_nodes/g" variable.tf
sed  -i  "s/dkube.json/$credential_file/g" variable.tf
echo $installer_user_passwd | sudo -S  rm -rf terraform.tfstate terraform.tfstate.backup
#Init Terraform
./terraform init
#Apply Terraform
./terraform apply -auto-approve -no-color 

if [[ "${?}" -ne 0 ]];then
  echo "Something went wrong !! terroform apply Failed !!"
  exit 1
fi



echo $cluster_name
echo $project
echo $zone

#Connect to cluster
gcloud container clusters get-credentials $cluster_name --zone $zone --project $project


if [[ "${?}" -ne 0 ]];then
  echo "Something went wrong !! gcloud command failed !!"
  exit 1
fi


#Check for Docker if not installed, installed it
command -v docker
if [[ "${?}" -ne 0 ]];then
  VERSIONSTRING="5:18.09.2~3-0~ubuntu-bionic"
  echo "Docker does not exist\n"
  echo "installing Docker\n"
  sudo apt-get remove docker docker-engine docker.io containerd runc
  sudo apt-get -y update
  sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo apt-key fingerprint 0EBFCD88
  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt-get -y update
  sudo apt-get install docker-ce=$VERSIONSTRING docker-ce-cli=$VERSIONSTRING containerd.io
fi


echo $installer_user_passwd | sudo -S systemctl start docker
echo $installer_user_passwd | sudo -S docker login -u lucifer001 -p lucifer@dkube
echo $installer_user_passwd | sudo -S docker pull ocdr/dkubeadm:$DKUBEVERSION
echo $installer_user_passwd | sudo -S docker run --rm -t -v $HOME/.dkube:/root/.dkube ocdr/dkubeadm:$DKUBEVERSION init
echo $installer_user_passwd | sudo -S cp $HOME/install $HOME/.dkube/install

# Removing old keys
echo $installer_user_passwd | sudo -S rm $HOME/.dkube/ssh-rsa
echo $installer_user_passwd | sudo -S rm $HOME/.dkube/ssh-rsa.pub
echo $installer_user_passwd | sudo -S cp $public_key $HOME/.dkube/
echo $installer_user_passwd | sudo -S cp $private_key $HOME/.dkube/
echo $installer_user_passwd | sudo -S chown -R $installer_username:$installer_username $HOME/.dkube


#Check for kubectl.if not installed, installed it
command -v kubectl
if [[ "${?}" -ne 0 ]]; then
  echo "Kubectl does not exist\n"
  echo "Installing kubectl\n"
  curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
  chmod +x ./kubectl
  sudo mv ./kubectl /usr/local/bin/kubectl
  kubectl version
fi

sleep 150s

nodes=$(kubectl get no -o wide | awk '{if (NR!=1) {print $1}}')
if [[ "${?}" -ne 0 ]];then
        echo "Something went wrong !!"
        exit 1
fi
nodes=($nodes)
echo "$nodes"
externalip=$(kubectl get no -o wide | awk '{if (NR!=1) {print $7}}')
externalip=($externalip)
echo "$externalip"
internalip=$(kubectl get no -o wide | awk '{if (NR!=1) {print $6}}')
internalip=($internalip)
echo "$internalip"



cd $HOME/.dkube

#sed dkube.ini
sudo sed -i "/^\[REQUIRED\]/,/^PLATFORM=/s/=.*/=$platform/" dkube.ini
sudo sed -i "/^DISTRO=/s/DISTRO=.*/DISTRO=$DISTRO/" dkube.ini
sudo sed -i "/^USERNAME=/s/USERNAME=.*/USERNAME=$dkubeuser/" dkube.ini
sudo sed -i "/^PASSWORD=/s/PASSWORD=.*/PASSWORD=$dkubepass/" dkube.ini
sudo sed -i "s/DKUBE_NODE_NAME=.*/DKUBE_NODE_NAME=$nodes/" dkube.ini
sudo sed -i "s/STORAGE_DISK_NODE=.*/STORAGE_DISK_NODE=$nodes/" dkube.ini
cat dkube.ini

#sed k8s.ini
sudo sed -i "/^\[deployment\]/,/^provider=/s/=.*/=$platform/" k8s.ini
sudo sed -i "/^distro=/s/distro=.*/distro=$DISTRO/" k8s.ini
for((i=0; i<${#externalip[@]};++i));do sed -i "/^\[nodes\]/,/^#/s/#.*/${externalip[i]} ${internalip[i]}/" k8s.ini; done
sudo sed -i "/^\[ssh-user\]/,/^user=/s/=.*/=$GKE_cluster_username/" k8s.ini
cat k8s.ini


echo $installer_user_passwd | sudo -S  cp $HOME/.kube/config $HOME/.dkube/kubeconfig
echo $installer_user_passwd | sudo -S chown -R $installer_username:$installer_username $HOME/.dkube/kubeconfig

kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/ubuntu/daemonset-preloaded.yaml

sleep 3m

#Dkube Install
cd $HOME/.dkube
ls -larth $HOME/.dkube
echo $installer_user_passwd | sudo chmod 700 $HOME/.dkube/install
sudo ./install


