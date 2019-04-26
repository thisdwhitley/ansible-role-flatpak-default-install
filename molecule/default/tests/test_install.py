import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_flatpaks_installed(host):
    # I used to check with package.is_installed, that doesn't work with flatpak
    assert host.check_output('flatpak list') != "gedit"
    assert host.check_output('flatpak list') != "Clocks"
    assert host.check_output('flatpak remote-list') != "flathub"
    assert host.check_output('flatpak remote-list') != "gnome-apps"
