import bluebot

with bluebot.BlueBot('88:1b:99:16:e7:7d') as bot:
    for i in range(4):
        bot.forward()
        bot.left()
