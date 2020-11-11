# by Harsh & ME CAUSE ME NOOB , inspired by brain.py

import asyncio

from userge import userge


@userge.on_cmd("mod$", about={'header': "'.term names', '.term dadjoke --reddit', '.term pytuneteller pisces --today', '.term jotquote', '.term csvfaker -r 10 first_name last_name job', '.term kwot 5', '.term programmingquotes -l EN' "})
async def kill_func(message):
    animation_chars = [
        "P",
        "PO",
        "POR",
        "PORN",
        "PORNA",
        "PORNAG",
        "PORNAGE>",
        "DURABLE AS A LAWDA",
        "PORNAGE :",
        "<b>PORNAGE : DURABLE AS A LAWDA</b>",
    ]
    for i in range(10):
        await asyncio.sleep(0.6)
        await message.edit(animation_chars[i % 10], parse_mode="html")
