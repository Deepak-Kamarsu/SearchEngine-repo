from utils import TicToc, Tokenize, Helper, Console
from arguments import opt
import os
from SearchEngine import FileSearch
import concurrent.futures
from multiprocessing import cpu_count

tt = TicToc()
fs = FileSearch()


if __name__ == '__main__':
    try:   
        search_words = Tokenize.to_words(input("Type keywords to be searched in the files: ")) 
        all_files = Helper.get_text_files(opt.path)
        result_counter = 0 
        search_result = {}    
        
        tt.tic()
        with concurrent.futures.ProcessPoolExecutor(max_workers = cpu_count()-2) as executor:
            for result in executor.map(fs.search_for_words, all_files, [search_words]*len(all_files)):
                result_counter += 1
                print(f'Search completed {result_counter}({len(all_files)})...')
                _, file_name = os.path.split(result[0])
                search_result[file_name] = result[1]    
        Console.clear()    
        tt.toc("Search completed in")
        
        filterd_results = Helper.get_sorted_values(search_result, int(opt.show_filter))
        print(f'\n***********************\nThe top {opt.show_filter} matches are: \n***********************')
        for result in filterd_results:        
            print(f'{result[0]} : {result[1]} %')
            
    except Exception:
        print('Something went wrong. Please contact the administrator')
    
    
    