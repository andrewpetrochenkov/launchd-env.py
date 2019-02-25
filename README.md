[![](https://img.shields.io/pypi/pyversions/launchd-env.svg?longCache=True)](https://pypi.org/project/launchd-env/)
[![](https://img.shields.io/pypi/v/launchd-env.svg?maxAge=3600)](https://pypi.org/project/launchd-env/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-env.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-env.py/)

#### Install
```bash
$ [sudo] pip install launchd-env
```

#### Functions
function|`__doc__`
-|-
`launchd_env.read(path)`|return a dictionary with plist file environment variables
`launchd_env.write(path, **vars)`|write environment variables to a plist file

#### CLI
usage|`__doc__`
-|-
`python -m launchd_env.add plist_file env_file ...`|add environment variables from env file(s)
`python -m launchd_env.set plist_file env_file ...`|set environment variables from env file(s)

#### Examples
`~/LaunchAgents/.env`
```bash
PATH=/Users/username/.local/share/bin
```

```bash
$ python -m launchd_env.set ~/LaunchAgents/agent.plist ~/LaunchAgents/.env
```

`~/LaunchAgents/agent.plist`
```xml
...
<key>EnvironmentVariables</key>
<dict>
    <key>PATH</key>
    <string>/Users/username/.local/share/bin</string>
</dict>
...
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>