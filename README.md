# 세팅하기

## 개발 환경



## Miniconda3

```bash
mkdir ~/Downloads && cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh
설치경로
/opt/miniconda3
```

```bash
# console prompt
export PS1='\e[01;32m\u@\h \[\e[34m\]\w \[${c_sgr0}\]\[$(branch_color)\]$(parse_git_branch)\[${c_sgr0}\]\n> '

alias l='ls -lt'
alias la='ls -alt'
alias c='clear'
alias ..='cd ..'
alias ...='cd ../../'

# git setting
parse_git_branch()
{
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
c_cyan=`tput setaf 6`
c_red=`tput setaf 1`
c_green=`tput setaf 2`
c_sgr0=`tput sgr0`
branch_color ()
{
   if git rev-parse --git-dir >/dev/null 2>&1
   then
      color=""
      if git diff --quiet 2>/dev/null >&2
      then
         color="${c_green}"
      else
         color=${c_red}
      fi
   else
      return 0
   fi
   echo -ne $color
}
```

환경변수 등록

```bash
vim ~/.profile
export PATH=/opt/miniconda3/bin:/opt/miniconda3/condabin:$PATH
source ~/.profile

conda -V
conda config --set auto_activate_base False
```

파이썬 3.10 환경 등록

```bash
conda create -n py10 python=3.10 -y
conda env list
conda activate py10
source ~/.profile
```

## FastAPI

```bash
# conda 업데이트
conda update -n base -c defaults conda -y

# 최신버전 설치하기
conda install conda-forge::fastapi -y
conda upgrade fastapi -y
pip install passlib[bcrypt]
pip install "python-jose[cryptography]"

# 필수설치
conda install uvicorn -y
conda install jinja2 -y
conda install python-dotenv -y
conda install requests -y
conda install openai -y
conda install starlette -y

# Mysql Python 설치
conda install -c conda-forge mysql -y
conda install conda-forge::mysql-connector-python -y
conda install conda-forge::mysqlclient -y
conda install anaconda::sqlalchemy -y
conda install conda-forge::python-multipart -y

# 특정 버전 설치
pip install bcrypt==4.0.1
conda install pydantic=2.0.3 -c conda-forge -y
pip install pydantic[email]
```

로그인 SECRET_KEY 생성하기

```bash
python
import secrets
secrets.token_hex(32)
```

## Mysql

설치

```bash
# 윈도우 Mysql 과 충돌 안나게 하기
sudo apt install mysql-server -y

# 설치 후 시작해야 한다
sudo service mysql start

# 디비 생성 및 권한 부여를 한다
use mysql;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
flush privileges;
CREATE DATABASE upj53db DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER upj53@'localhost' identified by '';
CREATE USER upj53@'%' identified by '';
GRANT ALL PRIVILEGES ON upj53db.* TO 'upj53'@'localhost';
GRANT ALL PRIVILEGES ON upj53db.* TO 'upj53'@'%';
flush privileges;

# 설정하기
mysql_secure_installation
sudo systemctl enable mysql
sudo systemctl start mysql

# 에러가 발생한다면
su: warning: cannot change directory to /nonexistent: 그런 파일이나 디렉터리가 없습니다
# Ubuntu
sudo service mysql stop
sudo usermod -d /var/lib/mysql/ mysql
sudo service mysql start
```

외부접속 허용

```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
#bind-address 주석하기
sudo service mysql restart
```

우분투 Time Zone 한국으로 변경하기

```bash
# 1. 현재 시간대(TimeZone) 목록 조회
dpkg-reconfigure tzdata

# 2. Asia 선택 후 Seoul 선택
# 6  <<< Asia 번호
# 69 <<< Sesoul 번호
```

Mysql Time Zone

[참고링크](https://jwkim96.tistory.com/23)

```bash
mysql -u root -p mysql
```

```sql
-- 타임존 검색
select @@global.time_zone, @@session.time_zone;
SET GLOBAL time_zone='Asia/Seoul';

-- 서울로 타임존 세팅
SET time_zone='Asia/Seoul';

-- 만약 타임존 데이터가 없다면 데이터 다운로드
-- https://dev.mysql.com/downloads/timezones.html
-- Non POSIX with leap seconds 파일 다운받기
-- 압축풀기

use mysql;

source [저장한 sql 파일의 절대 경로]
```

## Run Server

```bash
서버 시작하기
nohup uvicorn main:app --host 0.0.0.0 --port 80 --reload &
상태 확인
tail -f nohup.out
서비스 검색하기
lsof -i :80

서비스 종료하기
kill -9 PID번호
```

## HTTPS SSL 설정하기

```bash
# snap 설치
sudo apt install snapd
sudo snap install --classic certbot

# certbot 명령을 시스템에서 실행할 수 있도록 준비
sudo ln -s /snap/bin/certbot /usr/bin/certbot
certbot --version

# 80포트 서비스 중지하고 인증서 발급받기
sudo certbot certonly --standalone

# FastAPI HTTS 서비스 시작하기
# fullchain.pem 인증서 파일 → key.pem
# privkey.pem 키 파일 → cert.pem
uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem

# nohup uvicorn main:app --host 0.0.0.0 --port 80 --reload &
# ssh upj53@211.222.208.46
nohup uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem --reload &

# 80포트 → 443포트로 redirecting
sudo iptables -t nat -L
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 443
```

## SSH root 허용

```bash
sudo vi /etc/ssh/sshd_config

# root 사용자의 로그인 허용 여부. (yes, prohibit-password, forced-commands-only, no) 중에서 설정해야 합니다. 설정하지 않으면 prohibit-password 가 됩니다.
PermitRootLogin yes

# 비밀번호 로그인 허용 여부. (yes, no). 설정하지 않으면 yes 가 됩니다.
PasswordAuthentication yes

# ChallengeResponse 라는 특이한 인증 허용여부. (yes, no). 설정하지 않으면 yes 가 됩니다.
ChallengeResponseAuthentication no

# ssh 서비스 재시작
service sshd reload
```

## 프론트엔드 Svelte 개발환경

[NVM 설치](https://github.com/nvm-sh/nvm)

```bash
# nvm 설치
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# npm v16.17.1 설치
nvm install v16.17.1 
# svelte 설치
npm create vite@latest Svelte-Sample -- --template svelte
npm install
# VS Code 세팅하기
# Svelte 서버 실행하기
npm run dev -- --host 0.0.0.0 --port 5173
# 스벨트 라우터 설치
npm install svelte-spa-router
# 모든 패키지를 최신버전으로 업데이트
npm install -g npm-check-updates
# 설치 패키지
svelte-sample@0.0.0 /workspace/Svelte-Sample
├── @sveltejs/vite-plugin-svelte@3.0.1
├── bootstrap@5.3.2
├── marked@11.1.1
├── moment@2.30.1
├── qs@6.11.2
├── svelte-spa-router@4.0.1
├── svelte@4.2.9
└── vite@5.0.12
# 배포용 빌드
npm run build
# dist 폴더에 빌드 파일이 있음
dist/index.html
dist/assets/index.xxxxx.css
dist/assets/index.xxxxx.js
```

**FastAPI 서버에 frontend 폴더에 만들어 적용하기**

```python
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

# assets 폴더 마운트
app.mount('/assets', StaticFiles(directory='./frontend/xxxx'))

# 링크 만들기
@app.get('/my-frontend')
def my_frontend_index():
  return FileResponse('./frontend/xxxx/index.html')
```
