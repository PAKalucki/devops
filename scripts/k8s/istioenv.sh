#!/bin/bash
### script to install istioctl
set +e

### arg 1 version
mkdir -p $HOME/bin
cd $HOME/bin

echo "Starting setup for istio ${1}"
if [[ -d "$HOME/bin/istio-${1}" ]]
then
  echo "istio-${1} is already installed, updating symlinks"
  rm -f $HOME/bin/istioctl || true
  ln -s $HOME/bin/istio-${1}/bin/istioctl $HOME/bin/istioctl
else
  echo "istio-${1} is not installed, pulling new version and updating symlinks"
  curl -L https://istio.io/downloadIstio | ISTIO_VERSION=${1} TARGET_ARCH=x86_64 sh -
  rm -f $HOME/bin/istioctl || true
  ln -s $HOME/bin/istio-${1}/bin/istioctl $HOME/bin/istioctl
fi
echo "Setup complete"
istioctl version