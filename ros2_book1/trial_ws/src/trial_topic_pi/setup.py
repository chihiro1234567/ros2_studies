from setuptools import setup

package_name = 'trial_topic_pi'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='test',
    maintainer_email='test@todo.todo',
    description='Examples of publisher and subscriber.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher = trial_topic_pi.trial_publisher_pi:main", #add
            "subscriber = trial_topic_pi.trial_subscriber_pi:main" #add
        ],
    },
)
