# PiHole-DNS-Updater

Basic CLI interface to allow adding custom DNS entries to PiHole for reference to local systems.

This will help provide easy hostname access within the local network when using PiHole DNS on the machine.

## Usage

This application requires a `config.cfg` file with the contents:

```
[PiHole]
address=
auth=
```

Where **address** is the IP address of the PiHole instance (Should match your DNS)

**Auth** is the value of *WEBPASSWORD* in `/etc/pihole/setupVars.conf` retrieved from the PiHole instance itself.


### Commands usage

```
python3 PiHole-DNS-Updater.py COMMAND [options]
```

**COMMAND**:
- add IP hostname [--id]
- remove id
- list [--id]