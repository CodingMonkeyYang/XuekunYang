import os

# 软件词汇路径
from DST.domain_thesaurus.DomainThesaurus import DomainThesaurus

path1 = "data/"

# 通用词库general_vocab
path2 = "https://dumps.wikimedia.org/enwiki/latest/"

DEFAULT_OUT_DIR = os.path.dirname(os.getcwd())

dst = DomainThesaurus(domain_specific_corpus_path=path1,
                      general_vocab_path=path2,
                      outputDir=DEFAULT_OUT_DIR)
# extract domain thesauruss
my_thesaurus = dst.extract()


# 示例：
# start to extract domain thesaurus
# for different datasets,  you should set different parameters
# In this example, we use default parameters
# The "cleanEng.txt" and "general_vocab.json" are the files you download
dst = DomainThesaurus(domain_specific_corpus_path=os.path.join(DEFAULT_OUT_DIR, "cleanEng.txt"),
                      general_vocab_path=os.path.join(DEFAULT_OUT_DIR, "general_vocab.json"),
                      outputDir=DEFAULT_OUT_DIR)
eng_domain_thesaurus = dst.extract()