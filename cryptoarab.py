import json
import telebot
import os
from operator import itemgetter

CHANNEL1='-1002470251512'
CHANNEL2='-1002322218261'
OWNER_ID = '706405185'

bot=telebot.TeleBot('7282195822:AAEB25I9O9TUNi_Vz5PIfGYZSKj8-TkmTxw')

########## FIrst menu
def menu(id):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('حسابي 🆔')
    keyboard.row('الاحالات 🙌🏻')
    keyboard.row('الاحصائيات 📊')
    data= json.load(open('users.json','r'))
    bot_name = bot.get_me().username
    user_id = id
    user = str(user_id)

    if user not in data['referred']:
        data['referred'][user] = 0
    json.dump(data, open('users.json', 'w'))
    ref_msg= "اهلا بك في القائمة الرئيسية:\n\nشارك رابطك الخاص للحصول على احالات\n\n🔗 {}"
    ref_count = data['referred'][user]
    ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, id)
    msg = ref_msg.format(ref_link)
    bot.send_message(id, msg, parse_mode="HTML",
                     reply_markup=keyboard)


############ Sub check
def check1(id):

    check = bot.get_chat_member(CHANNEL1, id)
    if check.status != 'left':
            return True
    else:
            return False


def check2(id):

    check = bot.get_chat_member(CHANNEL2, id)
    if check.status != 'left':
            return True
    else:
            return False


########################################################################
@bot.message_handler(commands=['start'])
def start(message):
    user_1 = message.chat.id
    msg = message.text

    if msg == '/start':
        user = str(user_1)
        print("back to start")
        data = json.load(open('users.json','r'))
        if user in data['refer']:
            return menu(user_1)
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = user
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        keyboard= telebot.types.ReplyKeyboardMarkup(row_width=1)
        keyboard.add('تحقق')
        msgg =  "💎اهلا  في بوت مسابقة التون لقناة Crypto 3rb💎\n\n للمشاركة في المسابقة يجب عليك اولا الانضمام الى القناة:\n\n\n\nاضغط على 'تحقق' بعد انضمامك الى القناة ادناه⬇️⬇️"
        bot.send_message(user_1,"اهلا بك في مسابقة التون لقناة Crypto 3rb", parse_mode="HTML",
                     reply_markup=keyboard)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
                            text='🤼‍♂️ Crypto test Group', url='https://t.me/crypto_test_g'))

        msg_start= "⬇️ الرجاء اولا الاشتراك في القناة الموجودة ادناه  ⬇️"
        bot.send_message(user, msg_start,
                         parse_mode="HTML", reply_markup=markup)


    else:

        data = json.load(open('users.json', 'r'))
        user = message.chat.id
        user = str(user)
        refid = message.text.split()[1]
        for k in data['refer']:
            if user == k:
                return menu(user_1)
            else:
                pass
        if user not in data['referred']:
            data['referred'][user] = 0
            data['total'] = data['total'] + 1
        if user not in data['referby']:
            data['referby'][user] = refid
        if user not in data['id']:
            data['id'][user] = data['total']+1
        json.dump(data, open('users.json', 'w'))
        print(data)
        keyboard= telebot.types.ReplyKeyboardMarkup(row_width=1)
        keyboard.add('تحقق')
        msgg =  "💎اهلا  في بوت مسابقة التون لقناة Crypto 3rb💎\n\n للمشاركة في المسابقة يجب عليك اولا الانضمام الى القناة:\n\n\n\nاضغط على 'تحقق' بعد انضمامك الى القناة ادناه⬇️⬇️"
        bot.send_message(user_1,"اهلا بك في مسابقة التون لقناة Crypto 3rb", parse_mode="HTML",
                     reply_markup=keyboard)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
                            text='🤼‍♂️ Crypto test Group', url='https://t.me/crypto_test_g'))

        msg_start= "⬇️ الرجاء اولا الاشتراك في القناة الموجودة ادناه  ⬇️"
        bot.send_message(user, msg_start,
                         parse_mode="HTML", reply_markup=markup)







@bot.message_handler(commands=['lead'])
def lead(message):
    data=json.load(open('users.json','r'))
    for ke, value in data['username'].items():
        usid= ke
        usname= value
        refcount= data['referred'][usid]
        ms="اسم المسنخدم: {}   عدد الاحالات: {}"
        mss=ms.format(usname, refcount)
        mss+= "\n"
        bot.send_message(message.chat.id, mss)


















############ Buttons Keyb
#keybaord command
#@bot.message_handler(commands=['keyboard'])
#def send_keybaord(message):
#  # Create a keyboard markup
##  keyboard= telebot.types.ReplyKeyboardMarkup(row_width=1)
 # keyboard.add('heya')
  #keyboard.add('check')

  #send keyboard to user

 # bot.send_message(message.chat.id, 'please choose something', reply_markup=keyboard)


################ Inline keyb

################## to deal with calls (ex: inline key)

#
 #  if call.data == 'iheya':
 #    bot.send_message(call.message.chat.id, "Maybe More hsappy now")
 #  elif call.data == 'icheck':
 #    bot.send_message(call.message.chat.id, "its working just leave it")
 #  elif call.data == 'inocheck':
 #    bot.send_message(call.message.chat.id, "Fuckin leave it")

################### TO deal with messages
#for recieving message
@bot.message_handler(func=lambda message:True)
def handle_message(message):

  if message.text == 'تحقق':
    ch1 = check1(message.chat.id)
    ch2 = check2(message.chat.id)
    bot.delete_message(message.chat.id, message.message_id)
    if ch1 == True :
        if ch2== False:

            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(
                            text='🤼‍♂️ Crytpo test ', url='https://t.me/crypto_test_22'))

            msg_start= "⬇️ الرجاء الاشتراك في هذه القناة⬇️"
            bot.send_message(message.chat.id, msg_start,
                         parse_mode="HTML", reply_markup=markup)
        else:
            user_id= message.chat.id
            user= str(user_id)
            name=message.from_user.first_name
            fname=str(name)
            data = json.load(open('users.json','r'))
            if user not in data['refer']:
                data['refer'][user] = True
                print('user not in refer')
                if user not in data['username']:
                    data['username'][user]= fname
                if user not in data['referby']:
                    data['referby'][user] = user
                    print(data)
                    json.dump(data, open('users.json', 'w'))
                    print('referby ok')
                if int(data['referby'][user]) != user_id:
                    ref_id = data['referby'][user]
                    ref = str(ref_id)
                    print(f'this is the referred by id: {ref_id}')
                    if ref not in data['referred']:
                        data['referred'][ref] = 0
                        print(data['referred'][ref])
                    json.dump(data, open('users.json', 'w'))
                    data['referred'][ref] += 1
                    print(data['referred'][ref])
                    bot.send_message(
                        ref_id, "*🏧 حصلت على احالة جديدة ")
                    print("message sent to refferal")
                    json.dump(data, open('users.json', 'w'))
                    print('json dump ok')
                    return menu(user_id)
                else:
                    print("else1")
                    json.dump(data, open('users.json', 'w'))
                    return menu(message.chat.id)
            else:
                    print('esle 2')
                    json.dump(data, open('users.json', 'w'))
                    menu(message.chat.id)


    else :
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(
                            text='🤼‍♂️ Crypto test Group', url='https://t.me/crypto_test_g'))

        msg_start= "⬇️ الرجاء اولا الاشتراك في القناة الموجودة ادناه  ⬇️"
        bot.send_message(message.chat.id, msg_start,
                         parse_mode="HTML", reply_markup=markup)


  if message.text == 'الاحصائيات 📊':
    data = json.load(open('users.json','r'))
    user_id = message.chat.id
    user=str(user_id)
    maxref = max(data['referred'])
    msg_stat= "\nعدد مستخدمين البوت: {}"
    tot_users= data['total']
    msg=msg_stat.format(maxref, tot_users)
    bot.send_message(message.chat.id, msg)

  if message.text == 'حسابي 🆔':
    data = json.load(open('users.json', 'r'))
    fname= message.from_user.first_name
    user_id = message.chat.id
    user=str(user_id)
    ref_count = data['referred'][user]
    acc_msg="👤 اسم المستخدم: {}\n\n" + " معرف المستخدم: {}\n\n" + "🫂 عدد الاحالات: {}"
    msg=acc_msg.format(fname, user_id, ref_count)
    bot.send_message(message.chat.id, msg)

  if message.text == 'الاحالات 🙌🏻':
    data = json.load(open('users.json', 'r'))
    ref_msg = "⏯️ عدد الاحالات : {} مستخدمين\n\n\n\n🔗 رابط الاحالة: ⬇️\n{}"

    bot_name = bot.get_me().username
    user_id = message.chat.id
    user = str(user_id)

    if user not in data['referred']:
        data['referred'][user] = 0
    json.dump(data, open('users.json', 'w'))

    ref_count = data['referred'][user]
    ref_link = 'https://telegram.me/{}?start={}'.format(
            bot_name, message.chat.id)
    msg = ref_msg.format(ref_count, ref_link)
    bot.send_message(message.chat.id, msg, parse_mode="HTML")




if __name__ == '__main__':
    bot.polling(none_stop=True)
