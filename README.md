<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/launchd-env.svg?maxAge=3600)](https://pypi.org/project/launchd-env/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/launchd-env.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/launchd-env.py/actions)

### Installation
```bash
$ [sudo] pip install launchd-env
```

#### Examples
`~/Library/LaunchAgents/.env`
```bash
PATH=/Users/username/.local/share/bin
```

```bash
$ python -m launchd_env ~/Library/LaunchAgents/.env ~/Library/LaunchAgents/agent.plist
```

`~/Library/LaunchAgents/agent.plist`
```xml
...
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/Users/username/.local/share/bin</string>
</dict>
...
```

```bash
$ find ~/Library/LaunchAgents -name "*.plist" -print0 | xargs -0 python -m launchd_env ~/Library/LaunchAgents/.env
```

#### Related
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)
+   [`launchd-tag` - LaunchAgents Finder tags](https://pypi.org/project/launchd-tag/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>