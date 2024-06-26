from setuptools import setup, find_packages

setup(
    name='rfpextractor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "llama_index",
        "pypdf",
        "python-dotenv",
        "pdf-page-annotator"
    ],
    # Additional metadata about your package.
    author='Chinmay Shrivastava',
    author_email='cshrivastava99@gmail.com',
    description='#',
    long_description_content_type='text/markdown',
)