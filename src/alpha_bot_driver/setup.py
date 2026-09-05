from setuptools import setup
import os
from glob import glob

package_name = 'alpha_bot_driver'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosdev',
    maintainer_email='al.sapsan@yahoo.com',
    description='AlphaBot2-Pi ROS 2 driver',
    license='MIT',
    entry_points={
        'console_scripts': [
            'driver_node = alpha_bot_driver.driver_node:main',
        ],
    },
)
