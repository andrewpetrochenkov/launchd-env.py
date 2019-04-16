<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/launchd-env.svg?longCache=True)](https://pypi.org/project/launchd-env/)
[![](https://img.shields.io/pypi/v/launchd-env.svg?maxAge=3600)](https://pypi.org/project/launchd-env/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-env.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-env.py/)

#### Installation
```bash
$ [sudo] pip install launchd-env
```

#### Executable modules
usage|`__doc__`
-|-
`python -m launchd_env env_path plist_path ...` |set launchd.plist(s) environment variables

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

#### Related projects
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>