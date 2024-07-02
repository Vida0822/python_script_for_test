import pytest
import os 
import glob

@pytest.fixture(scope="module")
def test():
    file_path = './test_dir/test.txt'

    for file in glob.glob('*.txt') : 
        assert file == 'Hello python.txt'
    
    pass


# 스케쥴링 : 특정 시간에 특정 작업을 실행하도록 예약하는 것이다 
# => 주기적으로 실행해야 하는 작업(스크립트, 명령어)을 자동화 할 수 있다. 
# (리눅스 -> Cron )
# # 0 10 * * 1-5 python3 /home/uni/Workspace/project/auto-bot/pjt-crawler/crawler.py