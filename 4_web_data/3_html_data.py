from html.parser import HTMLParser

meta_count = 0

class MyHTMLParser(HTMLParser):
  def handle_comment(self, comment):
    print(f"Encountered comment: {comment}")
    pos = self.getpos() # returns line number and character position
    print(f"\tat line: {pos[0]}, position: {pos[1]}")

  def handle_starttag(self, start_tag, attrs):
    global meta_count
    if start_tag == "meta": meta_count += 1
    print(f"Encountered start tag: {start_tag}")
    pos = self.getpos() # returns line number and character position
    print(f"\tat line: {pos[0]}, position: {pos[1]}")
    if attrs.__len__() > 0:
      print("\tattributes:")
      for a in attrs:
        print(f"\t{a[0]} = {a[1]}")

  def handle_endtag(self, end_tag):
    print(f"Encountered end tag: {end_tag}")
    pos = self.getpos() # returns line number and character position
    print(f"\tat line: {pos[0]}, position: {pos[1]}")

  def handle_data(self, data):
    if data.isspace(): return
    print(f"Encountered data: {data}")
    pos = self.getpos() # returns line number and character position
    print(f"\tat line: {pos[0]}, position: {pos[1]}")

# instantiate parser and feed it some HTML
parser = MyHTMLParser()
f = open("sample.html")
if f.mode == 'r':
  contents = f.read()
  parser.feed(contents)

print(f"meta tags found: {meta_count}")