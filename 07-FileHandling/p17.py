oryginal_file = open("text_to_copy.txt","r")
copy_file = open("copy_by_lines.txt","w")
for line in oryginal_file:
    copy_file.write(line)

oryginal_file.close()
copy_file.close()