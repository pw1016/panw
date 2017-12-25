import logging
import os

import jieba
from gensim import corpora, models, similarities
from gensim.corpora import Dictionary

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# """
# 激活日志
# Gensim使用Python标准的日志类来记录不同优先级的各种事件
# """

dictionary_file = 'D:/gensim/dictionary.txt'
corpus_file = 'D:/gensim/corpus.mm'
stop_dict_file = 'D:/gensim/jieba_dict/stop_words.dic'
user_dict_file = 'D:/gensim/jieba_dict/user_dict.dic'


# jieba.load_userdict(user_dict_file)


def check(text, analyse=False):
    """
    检测文本在语料库中的相似文档
    注意： 如果进行分词，应该和训练语料库的分词器使用同一个，否则检测的结果可能不准确
    :param text: 待检测的文本，如果是已经分词好的，text应该为一个列表，同时analyse设置为False，否则设置为True进行分词
    :param analyse: 是否需要分词，默认False。如果True，则调用Jieba进行分词，需要预先配置好相关字典，同时text为原始文件字符串
    :return:
    """
    if text is None:
        logging.error("待检测文档为空")
        raise RuntimeError("待检测文档为空")

    # 加载语料库
    corpus = list(corpora.MmCorpus(corpus_file))
    dictionary = Dictionary.load_from_text(dictionary_file)

    # 语料库转成TF-IDF模型
    tfidf_model = models.TfidfModel(corpus)
    corpus_tfidf = tfidf_model[corpus]
    '''
    TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降
    '''

    if analyse is True:
        terms = cut(text)
    else:
        terms = text

    # 处理要检测的文本
    text_corpus = dictionary.doc2bow(terms)  # 转换成bow向量
    text_corpus_tfidf = tfidf_model[text_corpus]  # 计算在语料库中的TF-IDF值

    """
    similarities.MatrixSimilarity类仅仅适合能将所有的向量都在内存中的情况。
    例如，如果一个百万文档级的语料库使用该类，可能需要2G内存与256维LSI空间。 
    如果没有足够的内存，你可以使用similarities.Similarity类。该类的操作只
    需要固定大小的内存，因为他将索引切分为多个文件（称为碎片）存储到硬盘上了。
    它实际上使用了similarities.MatrixSimilarity和similarities.SparseMatrixSimilarity两个类，
    因此它也是比较快的，虽然看起来更加复杂了。
    """

    # TF-IDF模型建立语料库索引
    similarity_tfidf = similarities.Similarity(None, corpus_tfidf, num_features=10000, num_best=3)
    # 检测相似度
    result1 = similarity_tfidf[text_corpus_tfidf]

    # 语料库转成LSI模型
    lsi_model = models.LsiModel(corpus_tfidf)
    corpus_lsi = lsi_model[corpus_tfidf]
    """
    如果两个单词之间有很强的相关性，那么当一个单词出现时，往往意味着另一个单词也应该出现(同义词)；
    反之，如果查询语句或者文档中的某个单词和其他单词的相关性都不大，那么这个词很可能表示的是另外
    一个意思(比如在讨论互联网的文章中，Apple更可能指的是Apple公司，而不是水果)。
    LSA(LSI)使用SVD来对单词-文档矩阵进行分解。SVD可以看作是从单词-文档矩阵中发现不相关的索引变量(因子)，
    将原来的数据映射到语义空间内。在单词-文档矩阵中不相似的两个文档，可能在语义空间内比较相似。
    """

    # LSI模型建立语料库索引
    similarity_lsi = similarities.Similarity(None, corpus_lsi, num_features=10000, num_best=3)
    # 检测相似度
    text_corpus_lsi = lsi_model[text_corpus_tfidf]
    result2 = similarity_lsi[text_corpus_lsi]
    return result1, result2


def train(text, analyse=False):
    """
    训练语料库
    :param text: 训练的文本 如果是已经分词好的，text应该为一个列表，同时analyse设置为False，否则设置为True进行分词
    :param analyse: 是否需要分词，默认False。如果True，则调用Jieba进行分词，需要预先配置好相关字典，同时text为原始文件字符串
    :return:
    """
    # 分词
    if analyse is True:
        terms = cut(text)
    else:
        terms = text

    if os.path.exists(dictionary_file) and os.path.exists(corpus_file):
        dictionary = Dictionary.load_from_text(dictionary_file)
        dictionary.add_documents([terms])
        corpus = list(corpora.MmCorpus(corpus_file))
        # 计算文档对应的稀疏向量（这里是bow向量）并增加到语料库
        corpus.append(dictionary.doc2bow(terms))
    else:
        texts = [terms]
        dictionary = corpora.Dictionary(texts)
        # 每一篇文档对应的稀疏向量（这里是bow向量）
        corpus = [dictionary.doc2bow(t) for t in texts]
    corpora.MmCorpus.serialize(corpus_file, corpus)
    dictionary.save_as_text(dictionary_file)


def train_from_dir(dir):
    pass


def cut(text):
    if text is None:
        raise RuntimeError("文档为空")
    # # 加载自定义词典
    # if os.path.exists(user_dict_file) and os.path.isfile(user_dict_file):
    #     jieba.load_userdict(user_dict_file)

    # 分词
    terms = list(jieba.cut(text))
    if os.path.exists(stop_dict_file) and os.path.isfile(stop_dict_file):
        with open(stop_dict_file, encoding='UTF-8') as f:
            stop_words = set([line.strip() for line in f.readlines()])
            if len(stop_words) > 0:
                return [term for term in terms if term not in stop_words]
    return terms


if __name__ == '__main__':
    raw_documents = [
        '0据报道，南京江心洲污泥偷排或处置 不当而造成的污染问题，不断被媒体曝光，谢谢大家',
        '1面对美国金融危机冲击与国内 经济增速下滑形势，中国政府在2008年11月初快速推出“4万亿”投资十项措施',
        '2全国大面积出现的雾霾，使解决我国环境质量恶化问题的紧迫性得到全社会的广泛关注',
        '3大约是1962年的夏天吧，潘文突然出现在我们居住的安宁巷中，她旁边走着40号王孃孃家的大儿子，一看就知道，他们是一对恋人。那时候，潘文梳着一条长长的独辫',
        '4坐落在美国科罗拉多州的小镇蒙特 苏马有一座4200平方英尺(约合390平方米)的房子，该建筑外表上与普通民居毫无区别，但其内在构造却别有洞天',
        '5据英国《每日邮报》报道，美国威斯康辛州的非营利组织“占领麦迪逊建筑公司”(OMBuild)在华盛顿和俄勒冈州打造了99平方英尺(约9平方米)的迷你房屋',
        '6长沙市公安局官方微博@长沙警事发布消息称，3月14日上午10时15分许，长沙市开福区伍家岭沙湖桥菜市场内，两名摊贩因纠纷引发互殴，其中一人被对方砍死',
        '7乌克兰克里米亚就留在乌克兰还是加入俄罗斯举行全民公投，全部选票的统计结果表明，96.6%的选民赞成克里米亚加入俄罗斯，但未获得乌克兰和国际社会的普遍承认',
        '8京津冀的大气污染，造成了巨大的综合负面效应，显性的是空气污染、水质变差、交通拥堵、食品不安全等，隐性的是各种恶性疾病的患者增加，生存环境越来越差',
        '9 1954年2月19日，苏联最高苏维埃 主席团，在“兄弟的乌克兰与俄罗斯结盟300周年之际”通过决议，将俄罗斯联邦的克里米亚州，划归乌克兰加盟共和国',
        '10北京市昌平区一航空训练基地，演练   人员身穿训练服，从机舱逃生门滑降到地面',
        '11腾讯入股京东的公告如期而至，与三周 前的传闻吻合。毫无疑问，仅仅是传闻阶段的“联姻”，已经改变了京东赴美上市的舆论氛围',
        '12国防部网站消息，3月8日凌晨，马来西亚    航空公司 MH370航班起飞后与地面失去联系，西安卫星测控中心在第一时间启动应急机制，配合地面搜救人员开展对失联航班的搜索救援行动',
        '13新华社昆明3月2日电，记者从昆明市政府新闻办获悉，昆明“3·01”事件事发现场证据表明，这是一起由新疆分裂势力一手策划组织的严重暴力恐怖事件',
        '14在即将召开的全国“两会”上，中国政府将提出2014年GDP增长7.5%左右、CPI通胀率控制在3.5%的目标',
        '15中共中央总书记、国家主席、中央军委主席习近平看望出席全国政协十二届二次会议的委员并参加分组讨论时强调，团结稳定是福，分裂动乱是祸。全国各族人民都要珍惜民族大团结的政治局面，都要坚决反对一切危害各民族大团结的言行',
        '16中共中央总书记、国家主席、中央军委主席习近平看望出席全国政协十二届二次会议的委员并参加分组讨论时强调，团结稳定是福，分裂动乱是祸。全国各族人民都要珍惜民族大团结的政治局面，都要坚决反对一切危害各民族大团结的言行'
    ]

    # for item_text in raw_documents:
    #     train(item_text, True)


    # corpora_documents = []
    # for item_text in raw_documents:
    #     item_seg = cut(item_text)
    #     corpora_documents.append(item_seg)
    #
    text = "项目名称测试报告1.基本信息测试计划的来源document04.测试文档06.测试计划双创产品测试计划20170423测试用例的来源无测" \
           "试对象描述1.需求不明确2.测试环境与开发环境未分离，测试过程中开发会提交代码，要求测试重新构建测试版本。3.没有干净的初始数" \
           "据库4.测试的程序未经开发自测测试环境描述开发提供的108测试服务器环境测试人员朱月恒、杨璐、宋良敏、张怡、刘喆测试时间2017.4.20——2017.4.252." \
           "测试前提1.所有页面中的大数据文本框输入字符不超过100个字2.项目申报页面上传的附件不超过100M；大赛提交页面上传的附件不超过10M3.附件上传页面，一次上传的附件不超过" \
           "6个4.基础数据库中的数据不能做任何改动5.学校下只有一个学校管理员；学院下只能有一个学院秘书6.测试过程中，不能删除任何测试时增加的数据7.所有测试的用户数据从后台通过系统管理员添加8.所有" \
           "测试严格按照业务流程要求执行3.结果与建议基于2.测试前提的前提下，大赛（不包含项目变更）、项目、用户及流程管理、人才库模块的业务流程可走通。建议后期开发完善版本时，首先解决2.测试前提中的问题，" \
           "保证不在此前提下，业务流程可走通。4.缺陷记录请见jira中的bug库。地址：http://192.168.0.105:18080/(机构名称，2002Page1of1"
    result = check(text, True)
    print(result)

    # print(cut("我们 是好人"))
    # print(cut("我们是好人"))
    # print(cut("我们，是好人"))
