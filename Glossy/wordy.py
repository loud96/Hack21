import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS



file_content=open (r"C:\Users\Fabes\desktop\hackathon\new folder\lecture.txt").read()

stopwords = set(STOPWORDS)
stopwords.update(["comments", "go", "comment", "okay", "will", "text", "page", "sometimes", "now", "want", "see"])
print(sorted(stopwords))
wordcloud = WordCloud(font_path = r'C:\Windows\Fonts\Verdana.ttf', background_color = 'black', width = 1200,
                            stopwords=stopwords,
                            height = 1000,
                            colormap='twilight'
                            ).generate(file_content)

# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()
wordcloud.to_file('word cloud.png')
