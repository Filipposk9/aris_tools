from setuptools import setup, find_packages

setup(
    name="pdf_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
        "openpyxl",
        "PyMuPDF"
    ],
    entry_points={
        "console_scripts": [
            "pdf-tools=main:main_menu",
        ],
    },
    author="Filippos Kozanitis",
    author_email="filippos.kozanitis@icloud.com",
    description="A command-line tool for manipulating PDF files",
    long_description=open("docs/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/filipposk9/aris_tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)