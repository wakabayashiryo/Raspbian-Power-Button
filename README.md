# Raspberry Pi に電源ボタンを追加する

GPIO3には、Wake From Halt機能が実装されておりGPIO3をLOWにするだけでスリープ状態からOSを復帰できる。   
また、稼動状態からシャットダウンする機能は実装されていないので、python+deamonを使用して同じGPIO3がLOWになった時にシャットダウンするように実装した。
- 参考   
    [Raspberry Pi の Wake From Halt 機能について](https://blog.goo.ne.jp/nirami/e/888e66f6b7d4adee93f9c850b362787c)   
    [ラズパイでシャットダウンボタンを付ける(ついでに起動ボタン)](https://qiita.com/clses/items/e701c1cb6490751a6040)


## 電源ボタンの追加(起動、シャットダウン対応)
- プログラム   
    [powerbutton.py](./powerbutton.py)
- ピン配置   
    - GPIO3: モーメンタリスイッチ用(アクティブLOW)
    - GPIO4: スイッチ内臓のLED用(アクティブHIGH)

- サービスファイル詳細   
    powerbutton.service
    ~~~
    [Unit]
    Description=Power Button Daemon

    [Service]
    ExecStart = /usr/bin/python3 powerbutton.py
    Restart=always
    Type=simple

    [Install]
    WantedBy=multi-user.target
    ~~~

- deamon設定
    - serviceファイルをシステムフォルダにコピー   
        > sudo cp powerbutton.service /usr/lib/systemd/system/

    - powerbuttonサービスの自動起動設定
        > sudo systemctl enable powerbutton.service

    - デーモンの再起動
        > sudo systemctl daemon-reload

    - デーモンサービスの起動
        > sudo systemctl start powerbutton.service

    - ステータス確認
        > sudo systemctl status powerbutton.service

- 電源ランプに命を吹き込む&USBの電流制限を1.2Aに変更
    > sudo emacs /boot/config.txt

	以下を追加   
	~~~
	max_usb_current=1
	dtparam=pwr_led_trigger=heartbeat
	~~~