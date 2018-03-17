from server import handler,run,post
from server import RequestHandler

@handler("index")
def printL(req):
    with open('index.html', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return 200,{"Content-type":"text/html"}, data

@handler("af","POST")
def answerpost(req):
        data1=str(post(req))
        data1=data1[1:]
        data="<head><title>Done</title>"        
        data=data+"</head>"+"<center><big style='font-size:24px'>"+data1+"<br/><a href='index'>back</a></big></center></body>"
        return 200,{"Content-type":"text/html"}, data

@handler("abc","POST")
def answerpost1(req):
      data="<head><title>info</title></head>"
      data=data+"<center><div style='background-color:aqua;'><big style='font-size:36px'>"
      data=data+"this is an info page </br>if you're not in the space Program you'd better get away of here </div><br/>"
      data=data+"<a href='index'>back</a></big> <br/></center>"
      return 200,{"Content-type":"text/html"}, data
run()