import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_type(host):
    assert host.system_info.type == 'linux', 'Only the Linux operating system is supported!'


def test_rsyslod_daemon(host):
    # Set the daemon name
    package_name = "rsyslog"
    service_name = "rsyslog"

    # Check if the system has cron daemon installed, enabled, up and running
    assert host.package(package_name).is_installed, 'The %s package should be installed.' % package_name
    assert host.service(service_name).is_running, 'The %s daemon should be running.' % service_name
    assert host.service(service_name).is_enabled, 'The %s service should be enabled.' % service_name


def test_rsyslog_configuration(host):
    # Logratate configuration file must be in place
    configuration = host.file('/etc/rsyslog.conf')
    assert configuration.exists, 'The rsyslog.conf should exists'

    # Rsyslog configuration file must load everything from rsyslog.d
    assert configuration.contains('$IncludeConfig /etc/rsyslog.d'), 'Rsyslog should read settings from rsyslog.d!'

    # This file should present in the system
    conf_file = host.file('/etc/rsyslog.d/10-stunnel.conf')
    assert conf_file.exists, 'The 10-stunnel.conf file should be created.'
    assert conf_file.user == 'root'
    assert conf_file.group == 'root'
    assert conf_file.mode == 0o644

    listen_file = host.file('/etc/rsyslog.d/listen.conf')
    assert not listen_file.exists, 'The listen.conf file should be removed.'
