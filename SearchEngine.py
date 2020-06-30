import mmap

class FileSearch:
    
    def search_score(self, found_words, search_words):
        return (len(found_words) / len(search_words)) * 100
    

    def search_for_words(self, file, search_words):
        # print(f'Searching {file}...')        
        found_words = set()
        with open(file, 'r') as f:
            while True:
                data  = f.read(250000) #Chunks of 250KB. Potential problem could be that a word could be divided with a chunk.
                                       #<<TODO>> So need to have a own mechanism for handling such issues.
                    
                if not data:
                    break
                not_found_words = search_words - found_words
                
                if(len(not_found_words) == 0):
                    break
                for word in not_found_words:
                    if word.lower() in data.lower():
                        found_words.add(word)
            del data
        # print(f'Search completed for {file}') 
        return file, self.search_score(found_words, search_words)
    
    
    def searchByMMap(self, file, search_words):
        found_words = set()
        with open(file, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as data:
            for word in search_words:
                if data.find(str.encode(word)) != -1:
                    found_words.add(word)
        return file, self.search_score(found_words, search_words)
    
                
        