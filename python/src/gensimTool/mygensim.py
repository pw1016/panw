import logging
import os
from collections import defaultdict

import jieba
from gensim import corpora, models, similarities
from gensim.corpora import Dictionary

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
"""
激活日志
Gensim使用Python标准的日志类来记录不同优先级的各种事件
"""

dict_file = 'D:/dict.txt'
corpus_file = 'D:/corpus.mm'
stop_dic_file = 'D:/stop_words.dic'


def check(doc):
    """
    检查文档相似性
    :param text: 要检查的文档
    :return:
    """
    if doc is None:
        logging.error("待检测文档为空")
        raise RuntimeError("待检测文档为空")
    if not os.path.exists(corpus_file):
        logging.warning("语料库不存在")
        return
    # dictionary = corpora.Dictionary.load_from_text(dict_file)
    # 每一篇文档对应的稀疏向量（这里是bow向量）
    # corpus = [dictionary.doc2bow(doc) for doc in corpora_documents]

    corpus = corpora.MmCorpus(corpus_file)
    dictionary = Dictionary.from_corpus(corpus);
    tfidf_model = models.TfidfModel(corpus)
    '''
    TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降
    '''
    corpus_tfidf = tfidf_model[corpus]

    # 处理测试文本
    text_corpus = dictionary.doc2bow(cut(doc))  # 转换成bow向量
    text_corpus_tfidf = tfidf_model[text_corpus]  # 计算tfidf值

    """
    similarities.MatrixSimilarity类仅仅适合能将所有的向量都在内存中的情况。
    例如，如果一个百万文档级的语料库使用该类，可能需要2G内存与256维LSI空间。 
    如果没有足够的内存，你可以使用similarities.Similarity类。该类的操作只
    需要固定大小的内存，因为他将索引切分为多个文件（称为碎片）存储到硬盘上了。
    它实际上使用了similarities.MatrixSimilarity和similarities.SparseMatrixSimilarity两个类，
    因此它也是比较快的，虽然看起来更加复杂了。
    """

    similarity_tfidf = similarities.Similarity(None, corpus_tfidf, num_features=600, num_best=5)
    result1 = similarity_tfidf[text_corpus_tfidf]
    print(result1)

    lsi_model = models.LsiModel(corpus_tfidf)
    corpus_lsi = lsi_model[corpus_tfidf]

    similarity_lsi = similarities.Similarity(None, corpus_lsi, num_features=400, num_best=2)
    text_corpus_lsi = lsi_model[text_corpus_tfidf]
    result2 = similarity_lsi[text_corpus_lsi]
    print(result2)


def train(doc):
    """
    训练语料库
    如果语料库文件不存在，则新增；否则追加当前文档到语料库
    :param doc: 需要训练的文档
    :return:
    """
    # 分词
    terms = cut(doc)

    # 去停止词
    stoplist = load_stop_words(stop_dic_file)
    texts = [term for term in terms if term not in stoplist]

    # texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
    texts = [texts]
    print(texts)

    # # 去掉只出现一次的词
    # frequency = defaultdict(int)
    # for text in texts:
    #     for token in text:
    #         frequency[token] += 1
    # texts = [[token for token in text if frequency[token] > 1] for text in texts]

    if os.path.exists(corpus_file):
        # dictionary = corpora.Dictionary.load_from_text(dict_file)
        mmcorpus = corpora.MmCorpus(corpus_file)
        corpus = list(mmcorpus)
        dictionary = Dictionary.from_corpus(corpus)
        corpus.append(dictionary.doc2bow(terms))
    else:
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(corpus_file, corpus)
    print(list(corpus))




def train1(doc):
    # 分词
    documents = cut(doc)

    # 去停止词
    stoplist = load_stop_words(stop_dic_file)
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    # 去掉只出现一次的词
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1] for text in texts]

    dictionary = corpora.Dictionary(texts)
    dictionary.save(dict_file)


def load_stop_words(file):
    try:
        with open(file) as f:
            return set([line.strip().lower() for line in f.readlines()])
    except Exception as e:
        logging.error(e)
        return []


def cut(line):
    terms = list(jieba.cut(line))
    return terms


if __name__ == '__main__':
    raw_documents = [
        '0南京江心洲污泥偷排或处置不当而造成的污染问题，不断被媒体曝光',
        '1面对美国金融危机冲击与国内经济增速下滑形势，中国政府在2008年11月初快速推出“4万亿”投资十项措施',
        '2全国大面积出现的雾霾，使解决我国环境质量恶化问题的紧迫性得到全社会的广泛关注',
        '3大约是1962年的夏天吧，潘文突然出现在我们居住的安宁巷中，她旁边走着40号王孃孃家的大儿子，一看就知道，他们是一对恋人。那时候，潘文梳着一条长长的独辫',
        '4坐落在美国科罗拉多州的小镇蒙特苏马有一座4200平方英尺(约合390平方米)的房子，该建筑外表上与普通民居毫无区别，但其内在构造却别有洞天',
        '5据英国《每日邮报》报道，美国威斯康辛州的非营利组织“占领麦迪逊建筑公司”(OMBuild)在华盛顿和俄勒冈州打造了99平方英尺(约9平方米)的迷你房屋',
        '6长沙市公安局官方微博@长沙警事发布消息称，3月14日上午10时15分许，长沙市开福区伍家岭沙湖桥菜市场内，两名摊贩因纠纷引发互殴，其中一人被对方砍死',
        '7乌克兰克里米亚就留在乌克兰还是加入俄罗斯举行全民公投，全部选票的统计结果表明，96.6%的选民赞成克里米亚加入俄罗斯，但未获得乌克兰和国际社会的普遍承认',
        '8京津冀的大气污染，造成了巨大的综合负面效应，显性的是空气污染、水质变差、交通拥堵、食品不安全等，隐性的是各种恶性疾病的患者增加，生存环境越来越差',
        '9 1954年2月19日，苏联最高苏维埃主席团，在“兄弟的乌克兰与俄罗斯结盟300周年之际”通过决议，将俄罗斯联邦的克里米亚州，划归乌克兰加盟共和国',
        '10北京市昌平区一航空训练基地，演练人员身穿训练服，从机舱逃生门滑降到地面',
        '11腾讯入股京东的公告如期而至，与三周前的传闻吻合。毫无疑问，仅仅是传闻阶段的“联姻”，已经改变了京东赴美上市的舆论氛围',
        '12国防部网站消息，3月8日凌晨，马来西亚航空公司MH370航班起飞后与地面失去联系，西安卫星测控中心在第一时间启动应急机制，配合地面搜救人员开展对失联航班的搜索救援行动',
        '13新华社昆明3月2日电，记者从昆明市政府新闻办获悉，昆明“3·01”事件事发现场证据表明，这是一起由新疆分裂势力一手策划组织的严重暴力恐怖事件',
        '14在即将召开的全国“两会”上，中国政府将提出2014年GDP增长7.5%左右、CPI通胀率控制在3.5%的目标',
        '15中共中央总书记、国家主席、中央军委主席习近平看望出席全国政协十二届二次会议的委员并参加分组讨论时强调，团结稳定是福，分裂动乱是祸。全国各族人民都要珍惜民族大团结的政治局面，都要坚决反对一切危害各民族大团结的言行'
    ]


    for item_text in raw_documents:
        train(item_text)
    # check("南京江心洲污泥偷排”等污泥偷排或处置不当而造成的污染问题，不断被媒体曝光")
