Ansible Role: flatpak-default-install
=====================================

This is a very simple role that will add flatpak repositories and install
flatpaks.  I am shifting to flatpaks because it will hopefully alleviate some of
the pain of finding a latest version, creating a repo, etc for an application.
Mainly I am a sucker because they are the self-proclaimed
[The Future Of Apps On Linux](https://flatpak.org).

This role will be used for flatpaks that do not require any additional
configuration, simply install them and use them.  I *do* have quite a few that I
will want to customize a bit, so I hope to use this to do the repository setup
and flatpak install, then a different set of plays for the configuration...
This particular "role" is really two simple tasks but these are tasks I don't
want to have to do for every application.

I prefer to pass the variables "into" the role from the playbook versus by
including variable files.  This is because I hope to make the role usable by
other projects/roles.  I don't know if this logic makes sense or not, but I am
essentially attempting to remove the variables from the role itself.

Important Notes
---------------

* I am doing everything system wide (not per user) so the tasks require
  escalated privileges

Requirements
------------

* N/A

Role Variables
--------------

All of these variables should be considered **optional** however, be aware that
sanity checking is minimal (if at all):

* `flatpakrepo_urls`
  * the URL of a repository to enable system wide.  I contrive the name from the
    URL
* `flatpak_name`
  * you should be able to specify either the entire URL to a `flatpakref` or
    the unique DNS name that identifies the flatpak.  My preference is the DNS
    name because it is cleaner (and I haven't thoroughly tested the URL...)

Example Playbook
----------------

Example playbook with configuration options specified:

```yaml
- hosts: localhost
  connection: local
  roles:
    - role: flatpak-default-install
      flatpakrepo_urls:
        - https://sdk.gnome.org/gnome-apps.flatpakrepo
        - https://dl.flathub.org/repo/flathub.flatpakrepo
      flatpak_name:
        - com.bluejeans.BlueJeans
        - com.spotify.Client
```

Inclusion
---------

I envision this role being included in a larger project through the use of a
`requirements.yml` file.  So here is an example of what you would need in your
file:

```yaml
# get the flatpak-default-install role from github
- src: https://github.com/thisdwhitley/ansible-role-flatpak-default-install.git
  scm: git
  name: flatpak-default-install
```

Have the above in a `requirements.yml` file for your project would then allow
you to "install" it (prior to use in some sort of setup script?) with:

```bash
ansible-galaxy install -p ./roles -r requirements.yml
```

Testing
-------

I have flip-flopped between using Travis and molecule for testing my roles.  But
in the past it has kept me from moving forward.  So that is my crappy excuse for
not having set up testing for this simple role yet.  Sorry.

To-do
-----

* set up a testing process

References
----------

* <https://docs.ansible.com/ansible/latest/modules/flatpak_module.html>
* <https://docs.ansible.com/ansible/latest/modules/flatpak_remote_module.html>

License
-------

All parts of this project are made available under the terms of the [MIT
License](LICENSE).
