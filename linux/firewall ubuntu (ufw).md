# List ufw COMMAND
> ### Usage: ufw COMMAND

## Commands:
- `enable`                          enables the firewall
- `disable`                         disables the firewall
- `default ARG`                     set default policy
- `logging LEVEL`                   set logging to LEVEL
- `allow ARGS`                      add allow rule
- `deny ARGS`                       add deny rule
- `reject ARGS`                     add reject rule
- `limit ARGS`                      add limit rule
- `delete RULE|NUM`                 delete RULE
- `insert NUM RULE`                insert RULE at NUM
- `prepend RULE`                    prepend RULE
- `route RULE`                      add route RULE
- `route delete RULE|NUM`           delete route RULE
- `route insert NUM RULE`           insert route RULE at NUM
- `reload`                          reload firewall
- `reset`                           reset firewall
- `status`                          show firewall status
- `status numbered`                 show firewall status as numbered list of RULES
- `status verbose`                  show verbose firewall status
- `show ARG`                        show firewall report
- `version`                         display version information

## Application profile commands:
- `app list`                        list application profiles
- `app info PROFILE`                show information on PROFILE
- `app update PROFILE`              update PROFILE
- `app default ARG`                 set default application policy