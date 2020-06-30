import time
import os


class TicToc:
    def __init__(self):
        self.t = None

    def tic(self):
        self.t = time.time()

    def toc(self, name='Elapse Time'):
        assert self.t, 'You forgot to call tic()'
        t_sec = round(time.time() - self.t)
        (t_min, t_sec) = divmod(t_sec,60)
        (t_hour,t_min) = divmod(t_min,60) 
        print('{}: {}hour:{}min:{}sec'.format(name, t_hour,t_min,t_sec))
        

class Console:
    @staticmethod
    def clear():
        if os.name in ('nt','dos'):
            os.system("cls")
        elif os.name in ('linux','osx','posix'):
            os.system("clear")
        else:
            print("\n") * 120
            
class Tokenize:
    @staticmethod
    def to_words(sentence):
        for delim in [',',';'," "]:
            sentence = sentence.replace(delim, ' ')
        return set(sentence.split())
    
class Helper:
    @staticmethod
    def get_sorted_values(dict, filter=10):
        return sorted(dict.items(), key=lambda x: x[1], reverse=True)[:filter]
    
    @staticmethod
    def get_text_files(path):
        path += "" if path[-1] == "/" else "/"
        return [os.path.join(path, file)  for file in os.listdir(path) if file.endswith(".txt")]
