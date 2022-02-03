from vkbottle.bot import Bot, Message
from vkbottle.tools import PhotoMessageUploader
from vkbottle import Keyboard, KeyboardButtonColor, Text
from parser import SiteParser, DocumentParser
from pr_exceptions.abc_exceptions import BaseParserException
START_KEYBOARD = (Keyboard(inline=True)
                  .add(Text('Узнать изменения'), color=KeyboardButtonColor.POSITIVE)).get_json()

bot = Bot(input('Input group LongPoll API token: '))


@bot.on.message(lev=['Старт', 'Начать'])
async def start_handler(msg: Message):
    return await msg.answer('Приветствую! Жми на кнопки ниже. А, стоп, у меня же всего одна кнопка...',
                            keyboard=START_KEYBOARD)


@bot.on.message(lev=['Узнать изменения', 'Изменения'])
async def get_changes(msg: Message):
    try:
        sp = SiteParser('https://permaviat.ru/raspisanie-zamen/')
        last_file = await sp.last_file_link()
        filename = await sp.last_file_name()
        changes = await DocumentParser(last_file).find_changes()
    except BaseParserException as ex:
        args = '\n'.join(ex.args)
        return await msg.answer(f'Oops... Something wrong there. Description:\n{args}')
    text_response = f'{filename}:\n'
    if changes['changelist']:
        for change in changes['changelist']:
            text_response += f'{change["number"]} пара:\n➡{change["lesson_name"]}\n➡Препод: {change["teacher_name"]}\n'
        await msg.answer(text_response)
    if 'images' in changes.keys():
        if text_response == f'{filename}:\n':
            await msg.answer('Не удалось найти изменения, однако у меня тут есть скриншоты. Может быть, там что-то есть.')
        else:
            await msg.answer('Кстати, у меня есть еще и скриншоты. Посмотри их тоже.')

        for image in changes['images']:
            await msg.answer(attachment=await PhotoMessageUploader(bot.api).upload(image))
