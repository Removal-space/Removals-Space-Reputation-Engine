from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="removals-space-reputation-engine",
    version="1.0.0",
    author="Removals.Space",
    author_email="info@removals.space",
    description="Removals Space Reputation Engine is a digital reputation management and online content analysis tool designed to help individuals, businesses, and digital professionals better understand and manage their online visibility.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://removals.space",
    project_urls={
        "Homepage": "https://removals.space",
        "GitHub": "https://github.com/Removal-space/Removals-Space-Reputation-Engine",
        "Documentation": "https://removals-space-reputation-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/removals-space-reputation-engine",
    },
    py_modules=["reputation_engine"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "removals-space",
        "reputation-engine",
        "online-reputation-management",
        "digital-reputation",
        "content-removal",
        "serp-monitoring",
        "url-analysis",
        "search-visibility",
        "orm",
    ],
    entry_points={
        "console_scripts": [
            "removals-engine=reputation_engine:main",
        ],
    },
)
