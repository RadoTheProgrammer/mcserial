from setuptools import setup, find_packages

setup(
    name='mcserial',
    version='1.0.0',
    author='Rado Razakarivony',
    author_email='rado@arazakar.com',
    description='Turn pieces of minecraft world into objects or files',
    packages=find_packages(),
    install_requires=[
        "mcpi",
        "minecraftstuff",
        # List any dependencies your package requires
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)