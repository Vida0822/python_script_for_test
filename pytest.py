import pytest
import os 
import glob

@pytest.fixture(scope="module")
def test():
    file_path = './test_dir/test.txt'

    for file in glob.glob('*.txt') : 
        assert file == 'Hello python.txt'
    
    pass
