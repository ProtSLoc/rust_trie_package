# setup.py
from setuptools import setup, find_packages
from setuptools_rust import RustExtension, Binding

rust_extension = RustExtension("rust_trie.rust_trie", "rust_trie/Cargo.toml", binding=Binding.PyO3)

setup(
    name='rust_trie',
    version='0.1',
    packages=find_packages(),
    rust_extensions=[rust_extension],
    zip_safe=False,
)
