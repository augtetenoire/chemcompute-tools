from setuptools import setup, find_packages

setup(name='chemcompute',
      version='1.0',
      description='Package that contains the tools I developped to analyse the computational chemitry calculation I performed',
      url='https://github.com/augtetenoire/chemcompute-tools',
      author='Auguste TETENOIRE',
      author_email='auguste.tetenoire.pro@gmail.com',
      license='CNRS',
      packages=['chemcompute', 'chemcompute.ams', 'chemcompute.common', 'chemcompute.dftbplus', 'chemcompute.deepmd'],
      zip_safe=False)
