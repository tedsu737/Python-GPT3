# 匯入所需的庫
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 範例文本
text = """
Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability
with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming
paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often
described as a "batteries included" language due to its comprehensive standard library.
"""

# 生成文字雲
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# 顯示文字雲
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()