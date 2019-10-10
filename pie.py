from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Pie
from collections import Counter
from example.commons import Faker

dict = {'A':'马列毛',
'B': '哲学宗教',
'C': '社会科学总论',
'D': '政治、法律',
'E': '军事',
'F': '经济',
'G': '文化、科学、教育',
'H': '语言、文字',
'I': '文学',
'J': '艺术',
'K': '历史、地理',
'N': '自然科学总论',
'O': '数理科学与化学',
'P': '天文学、地球科学',
'Q': '生物科学',
'R': '医药、卫生',
'S': '农业科学',
'T': '工业技术',
'U': '交通运输',
'V': '航空航天',
'X': '环境安全',
'Z': '综合性图书'
}
class BingTu():
    s = []
    x = []
    y = []
    def get_info(self,info):
        for i in range(len(info)):
                self.s.append(info[i][0])
        c = Counter(self.s)
        c = c.most_common(5)
        for i in range(len(c)):
            self.x.append(c[i][1])
            self.y.append(dict[c[i][0]])
    def bin(self,info):
        self.get_info(info)
        pie =(
            Pie()
            .add("", [list(z) for z in zip(self.y,self.x)])
            .set_global_opts(title_opts=opts.TitleOpts(title="借阅分布"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return pie

    


