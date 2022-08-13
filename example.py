import bluebot

bot = bluebot.BlueBot('88:1b:99:16:e7:7d')

for i in range(4):
    bot.forward()
    bot.left()

bot.start()