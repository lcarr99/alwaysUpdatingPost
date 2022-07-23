import facebook
import datetime
from dateutil import parser
import os
from dotenv import load_dotenv

load_dotenv()

graph = facebook.GraphAPI(access_token=os.getenv("ACCESS_TOKEN"), version="2.12")

post = graph.get_object(os.getenv("POST_ID"));
now = datetime.datetime.now().astimezone()

created_time = parser.parse(post['created_time']);

diff = now - created_time;

graph.put_object(post['id'], '', message="I posted this " + str(round(diff.total_seconds() * 1000000)) + " microseconds ago!!");