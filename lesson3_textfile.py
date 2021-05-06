with open("exampletext.txt", "r") as sample_file:
    content = sample_file.read()
    print(content)

with open("exampletext.txt", "r") as sample_file_two:
    content_two = sample_file_two.read().splitlines()

    for line in content_two:
        print(line)

with open("text2.txt", "w") as sample_write:
    sample_write.write("Hallo, das ist ein Test")