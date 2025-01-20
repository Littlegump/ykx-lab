from setuptools import setup, find_packages

setup(
    name='ykx-lab',
    version='0.1.0',
    author='YinKaiXuan',
    author_email='yinkaixuan0213@gmail.com',
    description='A package for ykx lab',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/littlegump/ykx-lab',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        requests,
        flask,
        django,
    ],
)