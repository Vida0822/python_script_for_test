import os 
# 파이썬은 파일 및 디렉터리를 조작하는 기능 제공 
# => 대량의 파일을 처리하거나 복잡한 파일 시스템 작헙 자동화 가능 

 # 현재 작업 경로 확인 
curpath = os.getcwd()

# 작업 경로 바꾸기 
os.chdir('../')

# 하위 경로 만들기
path = os.path.join('./', 'os')

# 경로가 존재하는지 확인
os.path.isdir(path)

# 디렉터리 생성 
os.mkdir('./test_dir') # ./ : 현재 경로의
os.makedirs('./a/b/c', exist_ok=True)

# 파일 생성 
# +) 파이썬의 with : 자원 사용 후 반납해야하는 경우 사용 (자동 반납) ex) 파일, DB
with open('./test_dir/test_file.txt', 'w') as file:
    file.write('Hello Python')

# 파일 목록 확인 
os.listdir('./test_dir')

# 디렉터리 이동 
os.rename('test_dir', 'new_dir')

# 파일 이동 
os.rename('new_dir/test_file.txt', 'new_dir/moved_file.txt')

# 파일 삭제
os.remove('new_dir/moved_file.txt')

# 디렉터리 삭제
os.rmdir('new_dir')

# 파일 쓰기 
os.mkdir('./test_dir')
with open('./test_dir/test.txt', 'w') as file : # 쓰기모드 
    file.write('Hello, Python')

# 파일 읽기 
with open('test.txt' , 'r') as file : 
    print(file.read())

# 패턴 매칭 (glob)
# : 파일 시스템에서 특정 패턴에 일치하는 파일을 찾거나, 
# 파일 내용에서 특정 패턴은 찾는 것은 흔한 작업이다. 
import glob # 유닉스 셸 스타일의 패턴 매칭 

# glob
# 현재 디렉터리의 모든 txt 파일 찾기 
for file in glob.glob('*.txt') : 
    print(file)

# re
import re 

with open('test.txt', 'r') as file :
    contents = file.read()  # 파일 내용 읽어와서 (str)

# 파이썬이라는 단어 찾기 
matches = re.findall('Python', contents) # list
for match in matches : 
    print(match)



# shutil 라이브러리
import shutil 

# 파일 복사
fnames = os.listdir(os.getcwd())

for fname in fnames:
    src = os.path.join('./src_dir', fname)
    dst = os.path.join('./dst_dir', fname)

    shutil.copyfile(src,dst)

# 경로(폴더)와 파일 한꺼번에 삭제
shutil.rmtree('./')
