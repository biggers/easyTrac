from setuptools import setup
setup(
    name='trac_launcher',
    version='0.1',
    url='http://github.com/mviera/easyTrac',
    license='LGPLv3',
    description='Trac tool for running it through zc.buildout',
    author='Manuel Viera <manuel.viera.tirado@gmail.es>',
    classifiers=[
        'Development Status :: early stages',
        'Intended Audience :: Developers',
        'License :: EUPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    py_modules=['trac_launcher'],
    install_requires=[
        'distribute>=0.6.14',
    ],
)
