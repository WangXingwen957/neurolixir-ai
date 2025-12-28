from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent
README = (here / "README.md").read_text(encoding="utf-8") if (here / "README.md").exists() else "Neurolixir: lightweight rule-based chat utility."

setup(
    name="neurolixir",
    version="0.1.0",
    description="一个基于difflib和openai的轻量级规则匹配聊天工具",
    long_description=README,
    long_description_content_type="text/markdown",
    author="WangXingwen957",
    author_email="WangXingen333@163.com",
    url="https://github.com/WangXingwen957/neurolixir-ai",
    project_urls={
        "Source": "https://github.com/WangXingwen957/neurolixir-ai",
        "Tracker": "https://github.com/WangXingwen957/neurolixir-ai/issues",
    },
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    package_data={"neurolixir": ["gpt.txt"]},
    install_requires=[
        "pyttsx3>=2.90"
    ],
    extras_require={
        "openai": ["openai>=0.27.0"],
        "dev": ["pytest>=7.0", "pytest-cov", "setuptools-scm"]
    },
    entry_points={
        "console_scripts": [
            "neurolixir=neurolixir.neurolixir:start_chat"
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="chatbot rules fuzzy-matching openai neurolixir",
    license="MIT",
)