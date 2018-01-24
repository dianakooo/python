
def get_text(filename):
    ''' read file and return the text '''
    with open(filename, encoding = "utf-8") as file_object:
        text = file_object.read()
        return text


def tokenize(text):
    ''' tokenize the text '''
    words = text.split()
    return words


def extract_constr():
    ''' find np '''

    return constr_list


def write_results(constr_list, fname):
    with open (fname, 'w') as f:
        f.writelines(constr_list)
        #for constr in constr_list:
            #f.write(constr + '\n')


def main():
    #pipeline
    raw_text = get_text("sample_tagged_text.txt")
    #print(raw_text[:100])
    tokens = tokenize(raw_text)
    #print(tokens[:20])
    constr_list = extract_constr(tokens)
    for entry in constr_list:
        print(entry)
    write_results(constr_list, 'constr.txt')
    #tokenize()

main()
