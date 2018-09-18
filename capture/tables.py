import faust
import asyncio

from word_count.app import app

word_counts = app.Table('word_counts', default=int,
                        help='Keep count of words (str to int).')
