# SpeakerDeck-Slide-Image-Downloader
`https://speakerdeck.com/player/*`で示される形式のURL(例えば：[https://speakerdeck.com/player/fd822681129441c2ac6e8a62ae4634a9](https://speakerdeck.com/player/fd822681129441c2ac6e8a62ae4634a9))で見られるSpeaker DeckスライドはPDFでのダウンロードを行えませんが，これを使うと全てのスライドを画像として抽出しダウンロードすることができます．抽出した画像は[画像梱包](https://www.vector.co.jp/soft/win95/writing/se377893.html)などを使ってPDFにまとめることができます．
# 使い方
1. BeautifulSoupをインストールしてください．  
`$ pip install bs4`
2. sd-sid.pyを実行してください．
3. SpeakerDeckのプレイヤーのURLと，画像を出力するディレクトリの名前を入力してください．
4. スライド画像がダウンロードされていきます．
