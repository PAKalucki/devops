#!/bin/bash

sudo dnf update -y

echo "Installing and configuring tmux"
sudo dnf install -y tmux python-devel
grep -qF "tmux" ~/.bashrc || echo 'if command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then exec tmux; fi' >> ~/.bashrc

echo "Installing and configuring Ansible"
pip3 install ansible molecule docker-py --user
touch ~/.vault
grep -qF "ANSIBLE_VAULT_PASSWORD_FILE" ~/.bashrc || echo "export ANSIBLE_VAULT_PASSWORD_FILE=~/.vault" >> ~/.bashrc
grep -qF "ansible-playbook" ~/.bashrc || echo "alias ap='ansible-playbook'" >> ~/.bashrc

echo "Installing and configuring powerline"
pip install powerline-status --user
mkdir -p ~/.config/powerline

echo "Installing and configuring VS Code"
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf check-update
sudo dnf install code
code --install-extension vscoss.vscode-ansible
code --install-extension eamodio.gitlens
code --install-extension redhat.vscode-xml
code --install-extension ms-azuretools.vscode-docker
code --install-extension k--kato.intellij-idea-keybindings
code --install-extension ms-python.python

echo "Installing and configuring FZF"
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install --all
