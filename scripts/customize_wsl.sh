#!/bin/bash
MY_USER=prka
DOCKER=true
FZF=true
ANSIBLE=true
TMUX=true

set -e

for i in "$@"
do
case $i in
    -d=*|--extension=*)
    DOCKER="${i#*=}"
    shift
    ;;
    -f=*|--fzf=*)
    FZF="${i#*=}"
    shift
    ;;
    -a=*|--ansible=*)
    ANSIBLE="${i#*=}"
    shift
    ;;
    -t=*|--tmux=*)
    TMUX="${i#*=}"
    shift
    ;;
    *)
          # unknown option
    ;;
esac
done

echo "Customizing Ubuntu WSL for user $MY_USER"
id -u $MY_USER &>/dev/null || useradd $MY_USER 
echo "$MY_USER    ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
apt update -y && apt upgrade -y
apt install -y apt-transport-https \
              ca-certificates \
              curl \
              software-properties-common \
              python \
              python-pip \
              git \
              tmux \
              sshpass \
              rsync

if [ "$TMUX" = true ]
then
  echo "Configuring TMUX"
  sed -i '1ifi' /home/$MY_USER/.bashrc
  sed -i '1iexec tmux' /home/$MY_USER/.bashrc
  sed -i '1iif command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then' /home/$MY_USER/.bashrc
fi

if [ "$DOCKER" = true ]
then
  echo "Configuring Docker"
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
  apt update -y
  apt install -y docker-ce docker-compose
  usermod -aG docker $MY_USER
  echo "export DOCKER_HOST=tcp://localhost:2375" >> /home/$MY_USER/.bashrc
fi

if [ "$FZF" = true ]
then
  echo "Configuring FZF"
  git clone --depth 1 https://github.com/junegunn/fzf.git /home/$MY_USER/.fzf
  /home/$MY_USER/.fzf/install --all
fi

if [ "$ANSIBLE" = true ] 
then
  echo "Configure Ansible"
  pip install ansible argcomplete
  echo "alias ap='ansible-playbook'" >> /home/$MY_USER/.bashrc
fi

chown -R $MY_USER /home/$MY_USER