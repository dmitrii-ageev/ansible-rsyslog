RSYSLOG role for Ansible
========================

This role for deploying and configuring [RSYSLOG log processing server](http://www.rsyslog.com/) on Linux hosts using [Ansible](http://www.ansibleworks.com/).

Requirements
------------

No special requirements; note that this role requires root access.

Role Variables
--------------

rsyslog__modules: A list of rsyslog modules.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name    - The name of the module.
comment - Description of a module.
options - Configuration for a module.

rsyslog__config: A list of rsyslog configuration files and options.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
name    - The name of the file that goes into /etc/rsyslog.d/.
config  - Array of configuration options.

Here are config options:
comment - Description for a particular section.
options - Directives for rsyslog, view the rsyslog man page for specifics.

Dependencies
------------

None.

Example Playbook
----------------

This roles comes preloaded with everything required by default. You can override its variables in hosts/group vars, in your inventory, or in your play.
See the annotated defaults in `defaults/main.yml` for help in configuration. All provided variables start with `rsyslog__`.

Add this variable to your role's meta file like this:
```
# myrole/meta/main.yml
# 
dependencies:
  # Rsyslog settings
  - role: reannz.rsyslog
    when: rsyslog__state == "present"
    rsyslog__config:
      - file: "99-iptables-innd.conf"
        config:
          - comment: "This works, and the messages do get to iptables.log."
            options: |-
              :msg, regex,  "^\[ *[0-9]*\.[0-9]*\] IPT"  -/var/log/iptables.log
          - comment: "Logging for the INND system."
            options: |-
              news.crit                                   /var/log/news/news.crit
              news.err                                    /var/log/news/news.err
              news.notice                                -/var/log/news/news.notice
```

License
-------

GNU General Public License v2.0

Author Information
------------------

Dmitrii Ageev <dageev@gmail.com>
