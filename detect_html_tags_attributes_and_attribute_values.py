from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

        for attr in attrs:
            name, value = attr
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)

        for attr in attrs:
            name, value = attr
            print(f"-> {name} > {value}")


n = int(input())
s = [input() for _ in range(n)]

parser = MyHTMLParser()
for string in s:
    parser.feed(string)