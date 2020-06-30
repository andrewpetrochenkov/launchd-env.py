import setuptools

setuptools.setup(
    name='launchd-env',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
