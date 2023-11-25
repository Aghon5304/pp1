oryginal_file = open("text_to_copy.txt","r")
copy_file = open("copy.txt","w")
zawartosc_oryginalu= oryginal_file.read()
copy_file.write(zawartosc_oryginalu)

oryginal_file.close()
copy_file.close()