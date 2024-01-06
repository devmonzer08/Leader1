import re
import time
from datetime import datetime
from sourceklanr import StartTime, iqthon
from sourceklanr.Config import Config
from sourceklanr.plugins import mention
help1 = ("**⁂ ⦙ كيفيه التنصيب :**")
help2 = ("**⁂ ⦙ قـائمـه الاوامـر :**\n**⁂ ⦙ قنـاه السـورس :** @YYY4YI\n**⁂ ⦙ شـرح اوامـر السـورس : @YYY3YR** \n\n**❕- اوامر الاونلاين تشتغل فقط في مجموعات التخزين لاغير\n - اذا كنت تريد الاوامر العادية أرسل (.م) **")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My ⁂ {mention} ٫ **\n‌‎**⿻┊BoT ⁂ {TG_BOT} ٫**\n**‌‎⿻┊TimE ⁂ {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN ⁂ (8.3) ,** \n**⿻┊‌‎TeLeThoN AraB ⁂** @YYY4YI"
