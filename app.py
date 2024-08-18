from fasthtml.common import *

app, rt = fast_app()

count = 0

def getCount():
  return count

@rt("/increment")
def post():
  global count
  count += 1
  return count

@rt("/")
def get():
    return  Titled("FastHTML", 
              Group(
                P("Count: "),
                P(f"{count}",id="count")
              ),
              Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")        
            )

serve()