from setuptools import find_packages, setup

package_name = 'hello'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='KatsumiOuwa',
    maintainer_email='ouwa@emtechs.co.jp',
    description='hello world',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_node = hello.hello_node:main',
            'hello_publisher_node = hello.hello_publisher_node:main',
            'hello_subscriber_node = hello.hello_subscriber_node:main',
            'hello_fizz_buzz_node = hello.hello_fizz_buzz_node:main',
            'hello_service_node = hello.hello_service_node:main'
        ],
    },
)
