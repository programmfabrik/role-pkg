import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haveged(host):
    assert host.package('haveged').is_installed


def test_unattended_upgrades(host):
    assert host.package('unattended-upgrades').is_installed
    assert host.run('debconf-show unattended-upgrades | grep enable_auto_updates | grep -i "true"').rc == 0
