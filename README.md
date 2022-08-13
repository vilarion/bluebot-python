# BlueBot Python Module

Very simple python module to control a TTS BlueBot programmatically. As the example demonstrates, you only need the bot's MAC address to create an object. Just chain some commands and finally call the `start` method.

```python
import bluebot

bot = bluebot.BlueBot('88:1b:99:16:e7:7d')

for i in range(4):
    bot.forward()
    bot.left()

bot.start()
```

Alternatively you can use `with`:

```python
import bluebot

with bluebot.BlueBot('88:1b:99:16:e7:7d') as bot:
    for i in range(4):
        bot.forward()
        bot.left()
```