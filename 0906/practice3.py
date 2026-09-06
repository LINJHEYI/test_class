from telegram1 import Update

def main ():
    print(Update().message.reply_text('我是message實體的reply_text'))
if __name__ == '__main__':
    main()