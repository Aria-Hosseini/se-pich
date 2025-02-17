# Se-Pich Telegram Bot

## Introduction
This is a Telegram bot built using the `telebot` library. The bot provides administrative functionalities, such as welcoming new members, pinning/unpinning messages, banning/unbanning users, muting/unmuting members, deleting messages, locking/unlocking the group, and responding to specific keywords.

## Features
- **Welcomes new members** with a custom message.
- **Checks admin privileges** before executing admin commands.
- **Pins and unpins messages** when an admin replies to a message with "pin" or "unpin".
- **Bans users** when an admin replies to their message with a ban command.
- **Mutes and unmutes users** via admin commands.
- **Deletes messages** when an admin replies to a message with a delete command.
- **Locks and unlocks the group** to restrict or allow messages from non-admin users.
- **Replies to specific keywords** with predefined responses.

## Commands and Usage
### Admin Commands
| Command | Description |
|---------|-------------|
| `pin` / `پین` | Pins a replied message. |
| `unpin` / `آنپین` | Unpins a replied message. |
| `ban` / `بن` / `سیکتیر` | Bans the replied user. |
| `mute` / `ساکت` | Mutes the replied user. |
| `unmute` / `آزاد` | Unmutes the replied user. |
| `del` / `حذف` | Deletes the replied message. |
| `/lock` | Locks the group (only admins can send messages). |
| `/unlock` | Unlocks the group (all members can send messages). |

### Fun Commands
- The bot replies "جونم" when a user sends "سه پیچ".

## Installation
1. Install required dependencies:
   ```bash
   pip install pyTelegramBotAPI
   ```
2. Replace `Your Bot API token` with your actual Telegram Bot API token.
3. Run the bot:
   ```bash
   python bot.py
   ```

---

# ربات تلگرام سه پیچ

## معرفی
این ربات تلگرام با استفاده از کتابخانه `telebot` ساخته شده و امکانات مدیریتی مختلفی از جمله خوش‌آمدگویی، پین و آن‌پین پیام‌ها، بن کردن کاربران، سکوت و لغو سکوت، حذف پیام‌ها، قفل و باز کردن گروه و پاسخ به کلمات خاص را ارائه می‌دهد.

## قابلیت‌ها
- **خوش‌آمدگویی خودکار** به کاربران جدید.
- **بررسی دسترسی ادمین‌ها** قبل از اجرای دستورات مدیریتی.
- **پین و آن‌پین پیام‌ها** در صورت ریپلای کردن روی پیام و ارسال "pin" یا "unpin".
- **بن کردن کاربران** در صورت ریپلای کردن روی پیام و ارسال "بن" یا "سیکتیر".
- **سکوت و لغو سکوت کاربران** توسط ادمین‌ها.
- **حذف پیام‌ها** در صورت ریپلای کردن روی پیام و ارسال "حذف".
- **قفل و باز کردن گروه** برای محدود کردن یا اجازه ارسال پیام.
- **پاسخ به کلمات خاص** با پیام‌های از پیش تعیین‌شده.

## دستورات و نحوه استفاده
### دستورات ادمین
| دستور | توضیحات |
|---------|-------------|
| `pin` / `پین` | پین کردن یک پیام ریپلای شده. |
| `unpin` / `آنپین` | برداشتن پین از پیام ریپلای شده. |
| `ban` / `بن` / `سیکتیر` | بن کردن کاربر ریپلای شده. |
| `mute` / `ساکت` | ساکت کردن کاربر ریپلای شده. |
| `unmute` / `آزاد` | لغو سکوت کاربر ریپلای شده. |
| `del` / `حذف` | حذف پیام ریپلای شده. |
| `/lock` | قفل کردن گروه (فقط ادمین‌ها می‌توانند پیام ارسال کنند). |
| `/unlock` | باز کردن قفل گروه (همه کاربران می‌توانند پیام ارسال کنند). |

### دستورات سرگرمی
- در صورت ارسال "سه پیچ"، ربات پاسخ می‌دهد "جونم".

## نصب و راه‌اندازی
1. نصب وابستگی‌ها:
   ```bash
   pip install pyTelegramBotAPI
   ```
2. جایگزین کردن `Your Bot API token` با توکن واقعی ربات تلگرام.
3. اجرای ربات:
   ```bash
   python bot.py
   ```

