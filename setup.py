from distutils.core import setup

setup(
    name='rest-server',
    version='0.2.2',
    url="http://github.io/boundary/rest-server",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['restserver', ],
    entry_points={
        'console_scripts': [
            'rest-server = restserver.app:main',
        ]
    },
    package_data={'restserver': ['*.json', 'rest.*']},
    license='LICENSE',
    description='TrueSight Pulse Meter Plugin REST Target',
    long_description=open('README.txt').read(),
    install_requires=[
        "Flask >= 0.10.1"
    ],
)
