# voicevox.py
Python上から簡単にVORCEVOXの音声合成を利用できるモジュール。
## 最新版を利用する場合
最新版(ベータ版を含む)をダウンロードしたい場合は、Gitがインストールされていることが条件となります。
インストール時は以下のコマンドを実行してください。
`pip install git+https://github.com/sonyakun/voicevox.py.git`
### Github版利用の注意点
・不完全なモジュールの可能性があります。
・動作は保証できません。
## webAPIで利用する
音声合成(例)
```python
import voicevox
from voicevox import webapi

webapi.run(apikey="ApiKey Here",text="your text here",sound="3") #サウンドIDやApiKeyはWeb版VOICEVOXのサイトから確認してください
```
## クライアントのVOICEVOXで利用する(未実装)
```python
import voicevox
from voicevox import vbox_client

vbox.run(text="your text here")
```
