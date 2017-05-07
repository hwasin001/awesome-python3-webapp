import logging;logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body = b'<h1>Awesome</h1>')


# 异步函数，使用async/await

async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 获得 eventloop引用，将init函数（协程）放到eventloop中执行，这里只有一个协程
# event 负责 I/O 事件通知而 loop 负责循环处理 I/O 通知并在就绪时调用回调

loop=asyncio.get_event_loop()

# 协程自动封装成 task，放入eventloop中执行。

loop.run_until_complete(init(loop))

# 一直运行
loop.run_forever()