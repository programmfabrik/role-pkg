# Ansible Role Pkg

This role installs and configures arbitrary packages via APT.
It serves for all those cases where a dedicated role is just too much overhead.
Simply append to `pkg_list` and pull this role into your run to deploy a baseline of packages.
It supports files, templates and setting debconf variables before installation.

## Example Playbook

```yaml
- hosts: all
  become: yes
  vars:
    pkg_list:
      - name: haveged
      - name: unattended-upgrades
        debconf:
          - question: unattended-upgrades/enable_auto_updates
            vtype: boolean
            value: true
      - name: ntp
        templates:
          - name: etc/ntp.conf
            mode: 0644
            owner: root
            group: root
            
  roles:
     - role: blunix.role-pkg
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
