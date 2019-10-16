def get_read_text_line():
    f = open('text_list.txt', 'r')
    text_list = [t.replace("\n", "") for t in f.readlines()]
    # text_list = text_list * 200
    f.close()
    return text_list


if __name__ == '__main__':
    print(get_read_text_line())
