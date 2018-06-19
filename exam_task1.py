import csv
import os
import re

def main():
    with open("news.csv", "a", newline = "") as file:
        first_line = ["doc_id","title","author","created","topic","tagging"]
        writer = csv.writer(file)
        writer.writerow(first_line)
    start_path = 'news'
    fnames = os.listdir(start_path)
    #print(fnames)
    for fname in fnames:
        with open(os.path.join(start_path, fname), encoding = "utf-8") as f:
            text = f.read()
            match = re.search('content="(.*)" name="docid"', text)
            if match:
                doc_id = match.group(1)
                #print(doc_id)
            match = re.search('title\>(.*) \/', text)
            if match:
                title = match.group(1)
                match = re.search('\. (.*)', title)
                if match:
                    title = match.group(1)
                #print(title)
            match = re.search('content="(.*)" name="author"', text)
            if match:
                author = match.group(1)
                #print(author)
            match = re.search('content="(.*)" name="created"', text)
            if match:
                created = match.group(1)
                #print(created)
            match = re.search('content="(.*)" name="topic"', text)
            if match:
                topic = match.group(1)
                #print(topic)
            match = re.search('content="(.*)" name="tagging"', text)
            if match:
                tagging = match.group(1)
                #print(tagging)
            csv_file = [
                [doc_id, title, author, created, topic, tagging]
            ]
            with open("news.csv", "a", newline = "") as file:
                writer = csv.writer(file)
                writer.writerows(csv_file)

if __name__ == "__main__":
    main()

#названия, в которых присутствуют запятые, в csv-файле записываются в кавычках,
#и я не знаю, как это исправить, и надо ли исправлять вообще    
