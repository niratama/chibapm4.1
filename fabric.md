Fabricで楽しよう
----

こばやし けんいち

サーバ台数多くなるといろいろ面倒
----

* シェルスクリプトで
	* 複雑なことやらせるのは無理
* ChefとかPuppetとかある
	* 覚えること多かったり、使うまでにそれなりに手間かかる

Fabricとは
----

* シンプルなデプロイ・システム管理ツール
	* とりあえず始めるのに覚えることが少ない
* Python製で設定ファイルもPythonのスクリプト
	* いざとなればPythonで書けることはなんでもできる
	* Python 2.5以降が必要なのでCentOSでは別途インストールが必要
* SSH経由で他のサーバに乗り込んで作業ができる
	* 乗り込んだ先のマシンにいろいろインストールする必要はない

設定ファイル例
----

<?prettify lang=python?>

	from fabric.api import *

	def host_name():
	    run('hostname')

	def get_hosts():
	    get('/etc/hosts')

	def sudo_test():
	    run('whoami')
	    sudo('whoami')

設定ファイル
----

* fabfile.py という名前でファイルを用意する
* タスク = 関数
* 複数ファイルに分割してモジュール化できるので、規模がある程度大きくなっても安心

コマンドを実行する
----

	$ fab -H server1,server2 host_name
	[server1] Executing task 'host_name'
	[server1] run: hostname
	[server1] Passphrase for private key:
	[server1] out: server1
	[server1] out:
	[server2] Executing task 'host_name'
	[server2] run: hostname
	[server2] out: server2
	[server2] out:
	Done.

ファイルをダウンロードする
----

	$ fab -H server1,server2 get_hosts
	[server1] Executing task 'get_hosts'
	[server1] Passphrase for private key:
	[server1] download: /home/user/server1/hosts <- /etc/hosts
	[server2] Executing task 'get_hosts'
	[server2] download: /home/user/server2/hosts <- /etc/hosts
	Done.

sudoで実行する
----

	$ fab -H server1 sudo_test
	[server1] Executing task 'sudo_test'
	[server1] run: whoami
	[server1] Passphrase for private key:
	[server1] out: user
	[server1] out:
	[server1] sudo: whoami
	[server1] out: sudo password:
	[server1] out: root
	[server1] out:
	Done.

複数タスクを実行する
----
	$ fab -H server1 host_name get_hosts
	[server1] Executing task 'host_name'
	[server1] run: hostname
	[server1] Passphrase for private key:
	[server1] out: server1
	[server1] out:
	[server1] Executing task 'get_hosts'
	[server1] download: /home/user/server1/hosts <- /etc/hosts
	Done.

ホスト名の管理
----

* fabfile.py中では変数なので、設定ファイル中に埋め込むことも可能
* Roleでグループ化することも可能
* Pythonスクリプトなので、外部からホスト一覧を読み込むことも可能

その他できること
----

* コマンド実行結果の取り込み
* シェルの起動
* ファイルのアップロード
* rsync
* テンプレートを使ったテキストのアップロード
* 正規表現を使ったリモートファイルの修正

参考
----

* Fabricドキュメント <http://docs.fabfile.org/>
* Fabric 1.0日本語ドキュメント <https://fabric_ja.readthedocs.org/en/latest/>
* Python日本語ドキュメント <http://docs.python.jp/2/index.html>
* 今日からすぐに使えるデプロイ・システム管理ツール Fabric 入門 <http://d.hatena.ne.jp/shiumachi/20130414/1365920515>
* Python製デプロイツール Fabricを初めて使う際に役立つTips <http://dekokun.github.io/posts/2013-04-07.html>
* fabfileの構造化 <http://d.hatena.ne.jp/feiz/20110915/1316107432>
* Fabric デプロイツールのPythonicな書き方 <http://www.ianlewis.org/jp/fabric-pythonic>

<script src="https://google-code-prettify.googlecode.com/svn/loader/run_prettify.js"></script>
