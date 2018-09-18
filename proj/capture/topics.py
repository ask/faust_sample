import faust
import asyncio

from word_count.app import app

posts_topic = app.topic('posts', value_type=str)
