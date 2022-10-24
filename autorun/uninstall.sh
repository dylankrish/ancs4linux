#!/bin/bash
set -eu
set -x

if [ "$(whoami)" != "root" ]; then
    echo "Run this as root!"
    exit 1
fi

USER=${SUDO_USER:-root}
gpasswd --delete "$USER" ancs4linux
groupdel -f ancs4linux

cd "$(dirname "$0")"


systemctl stop ancs4linux-observer.service
systemctl stop ancs4linux-advertising.service

systemctl disable ancs4linux-observer.service
systemctl disable ancs4linux-advertising.service
systemctl --global disable ancs4linux-desktop-integration.service

rm /usr/lib/systemd/system/ancs4linux-observer.service
rm /usr/share/dbus-1/system.d/ancs4linux-observer.conf
rm /usr/lib/systemd/system/ancs4linux-advertising.service
rm /usr/share/dbus-1/system.d/ancs4linux-advertising.conf
rm /usr/lib/systemd/user/ancs4linux-desktop-integration.service

systemctl daemon-reload


set +e
deactivate
set -e
cd ..
pip3 uninstall ancs4linux
# Run as user:
# systemctl --user daemon-reload
# systemctl --user restart ancs4linux-desktop-integration.service


echo "Complete"
