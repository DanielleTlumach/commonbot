import datetime
import discord
from commonbot.utils import get_time_delta

class Timekeeper:
    def __init__(self):
        self.start_time = datetime.datetime.now()

    async def uptime(self, message: discord.Message, _):
        curr_time = datetime.datetime.now()
        days, hours, minutes, _ = get_time_delta(curr_time, self.start_time)
        mes = f"Я працюю вже {days} дні(в), {hours} год. та {minutes} хв."

        await message.channel.send(mes)
