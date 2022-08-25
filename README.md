# voicevox.py
Python上から簡単にVORCEVOXの音声合成を利用できるモジュール。
## 使い方
PC上のVOICEVOXを利用する
VOICEVOXダウンロード&インストーラー実行
```python
import voicevox
from voicevox import vboxclient
vboxapp = vboxclient.voiceclient() #Class「voiceclient」を利用可能にする
vboxapp.vbox_dl()#インストーラーをダウンロード&実行
```
VOICEVOXを起動
```python
import voicevox
from voicevox import vboxclient
vboxapp = vboxclient.voiceclient() #Class「voiceclient」を利用可能にする

vboxapp.app(exepass="VOICEVOXのexeの場所")
```
音声合成
```python
import voicevox
from voicevox import vboxclient
vboxapp = vboxclient.voiceclient() #Class「voiceclient」を利用可能にする

vboxapp.run(text="", speaker="3", filename="hoge")#textとfilenameは好きに変更できます
```
Web上のVOICEVOXのAPIを利用する
音声合成
```python
import voicevox
from voicevox import webapi

webapi.run(apikey="APIKeyは[ここから](https://su-shiki.com/api/)取得できます",text="",sound="3",filename="hoge")#textとfilenameは好きに変更できます
```
