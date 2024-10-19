# 匯入所需的庫
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 匯入正則表達式模組
import re

# 指定要分析的文本檔案路徑
file_path = r"C:\TED-DATA\TED-WORK\Python-Space\Python157207\Python-GPT3\Ted_Text.txt"
# 創建一個文本檔案相關類別的實例（模式"r"為唯讀），並指定給file這個變數後續可以操作指定的文本檔案
with open(file_path, "r", encoding="utf-8") as file:
    # 讀取文本內容，並用text這個變數接收回傳的內容字串
    text = file.read()

# # 範例文本
# text = """
# Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability
# with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming
# paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often
# described as a "batteries included" language due to its comprehensive standard library.
# """

# 生成文字雲
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 顯示文字雲
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()