# SearchEngine
**Description:**  This repository facilitates searching mechanism with a pre-scoped functionality. User input key-words are scanned across all the files(.txt) in a given directory.
                  *(found keywords / total search keywords)X100* is considered to be the top scorer in showing in the output. Like such by default top 10 matches will be shown.
          
**Input:**        *main.py* is the main file to run. In the python commandline interface, --help can be seen for the options to run the code.
                  ![](Images/help.JPG)      

**Input Example:**  The input parameters are the file path and the filtered results. The input key-words can be eighter with the delimeters(';' ' ', ',')
                  ![](Images/input.JPG)  
                  
**Output:**       The output looks like
                  ![](Images/output.JPG) 
                    
                  
**Technical highlights:**   
* Tested the search functionality with heavy text file sizes ***(50 GB)*** in a diretory, two files of them are ***23 GB*** each
* Used ***multi-processing***. A complete search/Scan on heavy files(50 GB) were done in 2-4 minutes. It works pretty fast(Seconds) if words found in initial/middle chunks. Thought tried ***multi-threading*** to make things concurrent as it involves IO bounds, it seems not have a significant impact so made the code to run on  ***multi-processing***
* ***MMAP and buffered chunks*** were tried to read such heavy data but opted bufferd chunks as MMAP has low performance on the complete setup.
* Code developed on Windows and hence tested on Windows and also tested on Linux. As 'os' module is used in the code, we need to make sure and needs testing it for running on different environments.
                   
                   
**Future improvements(TODO):**   
* Logging
* Performance in speed
* Extending to various file formats
* Input validations refinment
