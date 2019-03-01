def file_read(x):
        content_array = []
        with open(x) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)
        print(content_array[1:4])
file_read('678.txt')
