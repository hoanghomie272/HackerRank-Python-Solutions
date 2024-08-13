from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")

        for attr in attrs:
            name, value = attr
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}") 

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")

        for attr in attrs:
            name, value = attr
            print(f"-> {name} > {value}")


n = int(input())
s = [input() for _ in range(n)]

parser = MyHTMLParser()
for string in s:
    parser.feed(string)