# List ufw COMMAND
> ### Usage: ufw COMMAND

## Commands:
|command                    | description                       |
|---------------------------|-----------------------------------|
|`ufw enable`                 |enables the firewall               |
|`ufw disable`                |disables the firewall              |
|`ufw default ARG`            |set default policy                 |
|`ufw logging LEVEL`          |set logging to LEVEL               |
|`ufw allow ARGS`             |add allow rule                     |
|`ufw deny ARGS`              |add deny rule                      |
|`ufw reject ARGS`            |add reject rule                    |
|`ufw limit ARGS`             |add limit rule                     |
|`ufw delete RULE/NUM`        |delete RULE                        |
|`ufw insert NUM RULE`        |insert RULE at NUM                 |
|`ufw prepend RULE`           |prepend RULE                       |
|`ufw route RULE`             |add route RULE                     |
|`ufw route delete RULE/NUM`  |delete route RULE                  |
|`ufw route insert NUM RULE`  |insert route RULE at NUM           |
|`ufw reload`                 |reload firewall                    |
|`ufw reset`                  |reset firewall                     |
|`ufw status`                 |show firewall status               |
|`ufw status numbered`        |show firewall status as numbered list of RULES |
|`ufw status verbose`         |show verbose firewall status       |
|`ufw show ARG`               |show firewall report               |
|`ufw version`                | display version information       |

## Application profile commands:
|command                    | description                       |
|---------------------------|-----------------------------------|
|`ufw app list`               |         list application profiles |
|`ufw app info PROFILE`       |         show information on PROFILE |
|`ufw app update PROFILE`     |         update PROFILE |
|`ufw app default ARG`        |         set default application policy |