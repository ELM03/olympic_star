# olympic_star
SB Cloud Hackathon Repository

### アプリのインストール/ビルド方法 #####

#### SMS Server #####
apt-get install python
apt-get -y install python-dev
curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

apt-get install apache2
apt-get install libapache2-mod-wsgi

sudo apt-get install python-pip
sudo pip install MySQL-python
sudo apt-get install python-dev
sudo apt-get install libmysqlclient-dev

##### Android #####
下記にアクセスしてQRコードを読み取り
http://47.88.192.79/QRcode.gif

または、
http://47.88.192.79/olympic_star.apk
にアクセスして、ダウンロード後に
adb install olympic_star.apk


### アプリのテスト方法 #####

FLASK WEBサーバー(SMS送受信及びDrone位置情報取得用）の起動
/var/www/olympic_star/cgi-bin/run.py

SMSクライアントからのSMS送信


### オープンソースライブラリ一覧 #####
Server Side:
  Flask
  Twilio

Client Side:
  Google Map API
  Twilio

