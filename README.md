# Hello Cantonese

粵語，語文不一，導致很多粵語創作製作字幕難度比較大。
就算用聽寫軟件也只能做到自動生成粵語口語文本，也只能提供給懂粵語的朋友觀看，但講真，聽懂粵語的朋友又有多少需要看粵語字幕（除了特效字幕）？
想推廣粵語，就需要跟不懂粵語的朋友看書面語的中文字幕，但人手將口語轉為書面語工作量十分大，所以需要電腦幫忙。
Google 一直沒有推出 粵語-普通話 翻譯的API，所以此念頭一直擱置。
但最近恰巧發現百度翻譯 API 有 粵語-普通話 的翻譯，而且個人使用是免費的，因此可以開發一個小工具幫助大家（自己）把口語轉為書面語。


# 功能

此工具可將粵語口語 SRT 字幕文件翻譯並生成書面語 SRT 字幕文件，可以幫助粵語影片創作者節省製作字幕的時間。
就自己而言，以前做一條 10 分鐘影片的僅中文字幕需要 2 小時，但用這種方法生成字幕只需要 10 分鐘，包括簡繁英文版本。
SRT 是通用的字幕文件，可以上傳到各種支持 CC 字幕的平台上，例如 Youtube、Bilibili 等等。
有了這些字幕文件，就可以讓更多人願意觀看粵語影片，了解我們的語言，了解我們的文化。

### PyTranscriber
推薦配合 pyTranscriber 使用，簡單易容且免費，強烈推薦！ 
(GitHub) https://githujab.com/raryelcostasouza/pyTranscriber
pyTransciber 是一個利用 Google Speech Recognition API 將影片或語音文件自動生成字幕文件（SRT）的工具。
準確率因素材而異，但普遍可達 70%～80%，只需稍作改動就能理順語句。

提高識別率的方法：
* 避免在嘈雜的環境中收音。
* 剪接時，句子之間要留一定的"透氣位"，讓軟件識別如何斷句。
* 導出影片時生成一條沒有背景音樂及音效的影片。
* 語音音量均勻，尤其是最小聲的部分，可以在後期處理中適當提升音量。

### Cantonese CC
用 PyTranscriber 生成的 SRT 後，手動修改好錯誤的字幕或整理好語句，然後用 Cantonese CC 打開即可進行翻譯處理。
本工具僅提供 '粵-繁'、'粵-簡'及'中-英'翻譯。
'粵-繁''粵-簡'翻譯效果不錯，一般只需稍作修改即可使用。
中-英'翻譯質量還可以，但個人認為不能直接使用，要達至"通順"的要求還是需要一定時間修改。
不過從零開始翻譯是一項苦差，但如果有了基本翻譯草稿，然後通過人手修改和潤色，則可以大大提高效率。

提高翻譯準確率的方法：
* 百度的'粵-繁'翻譯是採用台灣詞彙，可能導致之後'中-英'翻譯準確率下降。
* 採用'粵-簡'翻譯，再用其他應用進行'簡-繁'切換，可能提高'中-英'翻譯的質量。
* 對語音識別結果先做處理，盡量把廣東話中的不影響句子意思語氣助詞刪除，例如句中停頓的"呢"，或者句頭的"咁"，或者句尾的"嘎喇嘛""個咯喔"等等。
* 進行'中-英'翻譯前，先將中文語句整理為通順的句子，英文翻譯質量將有顯著提升。

更多使用技巧不在此一一列舉，有時間的話再拍攝影片分享給大家。

# 使用前準備

### v0.2 新增登錄功能
用戶無需申請百度翻譯開發者賬號即可使用。由於是免費賬號，而且多人共享，多人同時使用時可能會出現請求超過限制的錯誤。
錯誤代碼為`{'error_code': '54003', 'error_msg': 'Invalid Access Limit'}`。
但是，一般來説，翻譯文章是一分鐘以内的事情，互相影響不會太大，因此請大家不要頻繁測試，以免影響其他朋友的使用。
若出現以上錯誤，稍後再試即可。
另外，共享賬號可能會過期的可能。
如果想徹底避免錯誤，可以自行申請百度翻譯開發者賬號。

### 註冊百度開發者帳號
使用前，需要註冊一個百度開發者帳號。
註冊網址： https://fanyi-api.baidu.com
高級版需要實名認證，不建议开通。建議註冊標準版即可。標準版只需提供手機號碼，完全免費，實現此功能完全夠用。
註冊並開通"百度翻譯"API服務後，進入 管理控制台 -> 開發者信息，即可獲得 appid（APP ID）及 secretkey（密鑰）。


# 使用方法

### （一）源代碼
Python 版本 3.6 (開發時使用，其他版本未測試。)

- 下載源代碼，並進入項目目錄。
```bash
git clone https://github.com/everyonepython/Cantonese_CC.git
cd Cantonese_CC
```

- 安裝此工具需要的 python 庫。
```bash
pip3 install -r requirements.txt
```

- 開啟軟件。
```bash
python3 main.py
```

### （二）執行文件
根據自己的操作系統，下載已打包好的軟件。
軟件發布地址：

> https://github.com/everyonepython/Cantonese_CC/releases

直接運行執行文件即可。


# 閒話

### 其他方法？
- 可以直接到百度翻譯界面進行翻譯。
https://fanyi.baidu.com/#yue/zh/

網頁翻譯限制在 5000 字節，如果用 srt 文件複製粘貼的話，由於有時間碼、符號及空行等等，很容易超過字數。而且，翻譯後格式會出現錯誤，需要重新排版。
因此，這個方法不會比自己人手翻譯快很多。

另外，它可以上傳文件進行翻譯，但不支持粵語。

- 期待 Google 可以推出粵語翻譯的 api。

