#!/usr/bin/env python
"""set launchd.plist(s) environment variables"""
import click
import launchd_env
import env_file

MODULE_NAME = "launchd_env"
USAGE = 'python -m %s env_path plist_path ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('env_path', required=True)
@click.argument('plist_paths', nargs=-1, required=True)
def _cli(env_path, plist_paths):
    for plist_path in plist_paths:
        data = launchd_env.plist.read(plist_path)
        data["EnvironmentVariables"] = env_file.get(env_path)
        launchd_env.plist.write(plist_path, data)


if __name__ == "__main__":
    _cli()
