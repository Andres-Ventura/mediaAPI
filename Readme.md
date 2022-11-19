@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    return {"message": "Successfully created post!"}

Explanation: This is going to extract all of the fields from the body (Body(...)) and convert it to a python dictionary (dict) and store it inside a variable named payload


*** Schema Validation with pydantic library ***

class Post(BaseModel):
    title: str 
    content: str

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    return {"data": "new post"} 

Output (Based on postman post request because we don't want to make a full front web application to initiate those post requests (Basically forms)):

Inputed in Postman: 
{
    "title": "look at me I'm flying!",
    "content": "check out-these awesome beaches"
}

Output: 
{
    "data": "new post"   
}

cursor_factory=RealDictCursor -> column name & value 


# using psycopg (hence the cursor.execute functionality)
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
# worth noting: while in postgres we would write the SQL as INSERT INTO <database name> (key variables) VALUES (values here)
# When actually interpreting postgres in python, the VALUES (values here) are act as placeholders %s 
# The placeholders %s prevent potential sql injection attacks
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    return {"data": post_dict}


conn.commit() - anytime you want to make a change to a database