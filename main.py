from fastapi import FastAPI, Response
from rubpy import Client, Rubino as BotDl
import asyncio
import json

app = FastAPI()

bot = Client("RubinoDl", "Your Auth")
Rubino = BotDl(bot)

@app.get("/RubinoDownloader/")
async def get_post_info(link: str):
    data = {"creator": "@Framework_Python"}
    try:
        await bot.connect()
        async with Rubino:
            result = await Rubino.get_post_by_share_link(link)
        post = result['post']
        data.update({
            "success": result['has_access'],
            "post_info": {
                "likes_count": post['likes_count'],
                "caption": post['caption'],
                "full_thumbnail_url": post['full_thumbnail_url'],
                "comment_count": post['comment_count'],
                "file_type": post['file_type'],
                "full_file_url": post['full_file_url'],
            }
        })
    except Exception as e:
        data.update({
            "success": False,
            "error": str(e)
        })
    finally:
        await bot.disconnect()
    return Response(content=json.dumps(data, ensure_ascii=False), media_type="application/json")
