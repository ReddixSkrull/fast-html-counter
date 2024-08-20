from fasthtml.common import *

app, rt = fast_app()

count = 0;

count = 0

def getCount():
  return count

@rt("/increment")
def post():
  global count
  count += 1
  return count

@rt("/")
def get(session, num: int):
    session.setdefault('count',0)
    session['count'] = session.get('count') + num
    return  Div(
                P("Count: " + f"{count}"),            
                Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")        
            )
    
serve()