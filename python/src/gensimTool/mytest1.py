import os

from gensimTool import mygensim

after_tika_dir = 'D:\\gensim\\after_tika'
records_file = 'D:\\gensim\\records.txt'


def my_train():
    with open(records_file, encoding='UTF-8', mode='a') as records:
        i = 0
        for file in [os.path.join(after_tika_dir, filename) for filename in os.listdir(after_tika_dir)]:
            if os.path.isfile(file):
                print("*" * 20)
                with open(file, encoding='UTF-8') as f:
                    line = f.read()
                    if line is not None:
                        print(line)
                        mygensim.train(line, analyse=True)
                        records.write(str(i) + '   ' + file + '\n')
                        i += 1


if __name__ == '__main__':
    # my_train()

    file = 'D:/gensim/after_tika_test/迭代总结.txt'
    with open(file, encoding='UTF-8') as f:
        text = f.read()
        print(text)
        result = mygensim.check(text, analyse=True)
        print(result)
