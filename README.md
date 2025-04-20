# mypage登録自動化のためのスクリプト

## 使い方

[`myProfile.json`](./myProfile.json)を編集して、以下の情報を入力してください。

> [!CAUTION]
> 休暇中の住所が現住所と異なる場合は、`AddressInVacation`の行を削除して下さい。
> 同じ場合は、`MyProfile > Text`の休暇中の部分は空の文字列にして下さい。

```
MyProfile
├── Text
│   ├── kname1:   姓
│   ├── kname2:   名
│   ├── yname1:   姓 (カタカナ)
│   ├── yname2:   名 (カタカナ)
│   ├── gyubin1:  現: 郵便番号上3桁
│   ├── gyubin2:  現: 郵便番号下4桁
│   ├── gadrs1:   現: 住所 (市区郡・地名・番地)
│   ├── gadrs2:   現: 住所 (アパート・マンション名・番号)
│   ├── kttel1:   現: 携帯電話番号上3桁
│   ├── kttel2:   現: 携帯電話番号中4桁
│   ├── kttel3:   現: 携帯電話番号下4桁
│   ├── kyubin1:  休暇中: 郵便番号上3桁
│   ├── kyubin2:  休暇中: 郵便番号下4桁
│   ├── kadrs1:   休暇中: (市区郡・地名・番地)
│   ├── kadrs2:   休暇中: (アパート・マンション名・番号)
│   ├── ktel1:    休暇中: 携帯電話番号上3桁
│   ├── ktel2:    休暇中: 携帯電話番号中4桁
│   ├── ktel3:    休暇中: 携帯電話番号下4桁
│   ├── bikoa:    研究室名
│   ├── bikob:    サークル名
│   ├── account1: メールアドレス (local part)
│   ├── domain1:  メールアドレス (domain part)
│   ├── account2: メールアドレス (local part)
│   ├── domain2:  メールアドレス (domain part)
│   ├── account3: 携帯メールアドレス (local part)
│   ├── domain3:  携帯メールアドレス (domain part)
│   ├── account3: 携帯メールアドレス (local part)
│   └── domain3:  携帯メールアドレス (domain part)
├── CheckBox
│   ├── ById
│   └── ByText
│       ├── AddressInVacation: 休暇中の住所が現住所と異なるなら、行を消す
│       └── Sex:               性別 (男 or 女)
└── Select
    ├── ByValue
    │   ├── ybirth: 生年月日（年）
    │   ├── mbirth: 生年月日（月） (一桁の時は0をつける)
    │   └── dbirth: 生年月日（日） (一桁の時は0をつける)
    └── ByText
        └── gken:   住所（都道府県）

GraduateSchool: 修士課程専用 (必要なければ消す)
└── CheckBox
    ├── ByText
    │   ├── SchoolClassification: 変えない
    │   ├── initial:              大学院名頭文字 (ひらがな)
    │   ├── location:             大学院所在地 (都道府県)
    │   ├── name:                 大学院名
    │   ├── faculty:              研究科名
    │   └── MajorClassification:  文理区分 (文系 or 理系)
    └── ById

University: 学部専用
├── CheckBox
│   ├── ByText
│   │   ├── classification: 変えない
│   │   ├── initial:        大学名頭文字 (ひらがな)
│   │   ├── location:       大学所在地 (都道府県)
│   │   ├── name:           大学名
│   │   ├── faculty:        学部名
│   │   └── department:     学科名
│   └── ById
└── Select
    ├── ByValue
    │   ├── sgnyear         入学年度
    │   ├── sgnmonth        入学月
    │   ├── sgsyear         卒業年度
    │   └── sgsmonth        卒業月
    └── ByText
```

## 実行

```bash
% python -m venv .venv
% source .venv/bin/activate
% pip install selenium    # もしくは pip install -r requirements.txt
% python autoregister.py [url]
```
`[url]`は、myPageのURLを指定してください。 \
例: `"https://mypage.3010.i-webs.jp/hoge2027/"`
