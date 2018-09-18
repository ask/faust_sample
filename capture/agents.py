import faust
import asyncio
from proj.app import app
from proj.capture.topics import posts_topic
from proj.capture.tables import word_counts

WORDS = ['the', 'quick', 'brown', 'fox']

@app.agent(posts_topic)
async def shuffle_words(posts):
    async for post in posts:
        for word in post.split():
            await count_words.send(key=word, value=word)

@app.agent(value_type=str)
async def count_words(words):
    async for word in words:
        word_counts[word] += 1

@app.page('/count/')
@app.table_route(table=word_counts, shard_param='word')
async def get_count(web, request):
    word = request.GET['word']
    return web.json({
        word: word_counts[word],
    })

@app.task
async def sender():
    for word in WORDS:
        for _ in range(1000):
            await shuffle_words.send(value=word)

    await asyncio.sleep(5.0)
    print(word_counts.as_ansitable(
        key='word',
        value='count',
        title='$$ TALLY $$',
        sort=True,
    ))

