# SpeakerDeck-Slide-Image-Downloader
`https://speakerdeck.com/player/*`で示される形式のSpeaker DeckスライドはPDFでのダウンロードを行えませんが，これを使うと全てのスライドを画像として抽出しダウンロードすることができます．抽出した画像は[画像梱包](https://www.vector.co.jp/soft/win95/writing/se377893.html)などを使ってPDFにまとめるることができます．
# 使い方
1. BeautifulSoupをインストールしてください．
`$ pip install bs4`
2. sd-sid.pyを実行してください．
3. `https://speakerdeck.com/player/*`形式のスライドのURLと，画像を出力するディレクトリの名前を入力してください．
4. スライド画像がダウンロードされていきます．