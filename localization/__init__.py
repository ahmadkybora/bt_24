# pylint: disable=line-too-long

START_MESSAGE = "START_MESSAGE"
START_OVER_MESSAGE = "START_OVER_MESSAGE"
HELP_MESSAGE = "HELP_MESSAGE"
ABOUT_MESSAGE = "ABOUT_MESSAGE"
DEFAULT_MESSAGE = "DEFAULT_MESSAGE"
ASK_WHICH_MODULE = "ASK_WHICH_MODULE"
ASK_WHICH_TAG = "ASK_WHICH_TAG"
ASK_FOR_ALBUM = "ASK_FOR_ALBUM"
ASK_FOR_ARTIST = "ASK_FOR_ARTIST"
ASK_FOR_TITLE = "ASK_FOR_TITLE"
ASK_FOR_GENRE = "ASK_FOR_GENRE"
ASK_FOR_YEAR = "ASK_FOR_YEAR"
ASK_FOR_ALBUM_ART = "ASK_FOR_ALBUM_ART"
ASK_FOR_DISK_NUMBER = "ASK_FOR_DISK_NUMBER"
ASK_FOR_TRACK_NUMBER = "ASK_FOR_TRACK_NUMBER"
ALBUM_ART_CHANGED = "ALBUM_ART_CHANGED"
EXPECTED_NUMBER_MESSAGE = "EXPECTED_NUMBER_MESSAGE"
CLICK_PREVIEW_MESSAGE = "CLICK_PREVIEW_MESSAGE"
CLICK_DONE_MESSAGE = "CLICK_DONE_MESSAGE"
CHANNEL_NOT_FOUND = "CHANNEL_NOT_FOUND"
LANGUAGE_CHANGED = "LANGUAGE_CHANGED"
MUSIC_LENGTH = "MUSIC_LENGTH"
REPORT_BUG_MESSAGE = "REPORT_BUG_MESSAGE"
ERR_CREATING_USER_FOLDER = "ERR_CREATING_USER_FOLDER"
ERR_ON_DOWNLOAD_AUDIO_MESSAGE = "ERR_ON_DOWNLOAD_AUDIO_MESSAGE"
ERR_ON_DOWNLOAD_VIDEO_MESSAGE = "ERR_ON_DOWNLOAD_VIDEO_MESSAGE"
ERR_ON_DOWNLOAD_PHOTO_MESSAGE = "ERR_ON_DOWNLOAD_PHOTO_MESSAGE"
ERR_ON_DOWNLOAD_LINK_MESSAGE = "ERR_ON_DOWNLOAD_LINK_MESSAGE"
ERR_TOO_LARGE_FILE = "ERR_TOO_LARGE_FILE"
ERR_ON_READING_TAGS = "ERR_ON_READING_TAGS"
ERR_ON_UPDATING_TAGS = "ERR_ON_UPDATING_TAGS"
ERR_ON_UPLOADING = "ERR_ON_UPLOADING"
ERR_NOT_IMPLEMENTED = "ERR_NOT_IMPLEMENTED"
ERR_OUT_OF_RANGE = "ERR_OUT_OF_RANGE"
ERR_MALFORMED_RANGE = "ERR_MALFORMED_RANGE"
ERR_BEGINNING_POINT_IS_GREATER = "ERR_BEGINNING_POINT_IS_GREATER"
BTN_TAG_EDITOR = "BTN_TAG_EDITOR"
BTN_CONVERT_VIDEO_TO_CIRCLE = "BTN_CONVERT_VIDEO_TO_CIRCLE"
BTN_CONVERT_VIDEO_TO_GIF = "BTN_CONVERT_VIDEO_TO_GIF"
BTN_MUSIC_TO_VOICE_CONVERTER = "BTN_MUSIC_TO_VOICE_CONVERTER"
BTN_CONVERT_VOICE_TO_AUDIO = "BTN_CONVERT_VOICE_TO_AUDIO"
BTN_MUSIC_CUTTER = "BTN_MUSIC_CUTTER"
BTN_BITRATE_CHANGER = "BTN_BITRATE_CHANGER"
BTN_ARTIST = "BTN_ARTIST"
BTN_TITLE = "BTN_TITLE"
BTN_ALBUM = "BTN_ALBUM"
BTN_GENRE = "BTN_GENRE"
BTN_YEAR = "BTN_YEAR"
BTN_ALBUM_ART = "BTN_ALBUM_ART"
BTN_DISK_NUMBER = "BTN_DISK_NUMBER"
BTN_TRACK_NUMBER = "BTN_TRACK_NUMBER"
BTN_BACK = "BTN_BACK"
BTN_NEW_FILE = "BTN_NEW_FILE"
MUSIC_CUTTER_HELP = "MUSIC_CUTTER_HELP"
NUMBER_OF_FILE_SENT = "NUMBER_OF_FILE_SENT"
DONE = "DONE"
FIRST_ADMIN_ME = "FIRST_ADMIN_ME"
OR = "OR"
SEND_TO_OTHERS = "SEND_TO_OTHERS"
SEND_TO_OTHERS_MESSAGE = "SEND_TO_OTHERS_MESSAGE"
SEND_TO_CHANNEL_MESSAGE = "SEND_TO_CHANNEL_MESSAGE"
SEND_TO_CHANNEL = "SEND_TO_CHANNEL"
SEND_CHANNEL_NAME_WITH_ID = "SEND_CHANNEL_NAME_WITH_ID"
REPORT_BUG_MESSAGE_EN = "That's my fault! Please send a bug report here: @jojo"
REPORT_BUG_MESSAGE_FA = "این اشتباه منه! لطفا این باگ رو از اینجا گزارش کنید: @jojo"
EG_EN = "e.g."
EG_FA = "مثل"

keys = {
    START_MESSAGE: {
        "en": "Hello there! 👋\n"
              "I'm music jojo; we can do the following together 👇\n\n\n"
              "💿 display and change the complete song profile \n"
              "✂️ Sampling and cutting the song and converting it to voice \n"
              "🏞 delete and change the song cover \n"
              "🎥 convert video to circular video \n"
              "📷 convert video to gif \n"
              "🔊 Convert voice to song \n"
              "📝 change the caption and remove ads \n\n\n"
              "⏪ Send post and file without name to channel \n\n\n"
              "⏪⏪⏪The following will be added in the future \n\n\n"
              "🎵 find song from video \n"
              "📥 Download the song through the download link \n"
              "📥 Download videos from all links like YouTube, Instagram, etc. \n"
              "📥 Download video via Instagram link \n\n\n"
              "⚠️ To start, please send a song/video: (You can download or upload directly!)",
        "fa": "سلام! 👋\n"
              "موزیک جوجو هستم؛ می‌تونیم کارای زیر رو باهم انجام بدیم 👇\n\n\n"
              "💿 نمایش و تغییر مشخصات کامل آهنگ \n"
              "✂️ نمونه‌گیری و برش آهنگ و تبدیل به وویس \n"
              "🏞 حذف و تغییر کاور آهنگ \n"
              "🎥 تبدیل ویدیو به ویدیو دایره‌ای \n"
              "📷 تبدیل ویدیو به گیف \n"
              "🔊 تبدیل وویس به آهنگ \n"
              "📝 تغییر کپشن و حذف تبلیغات \n\n\n"
              "⏪⏪⏪موارد زیر در آینده اضافه میشوند \n\n\n"
              "⏪ ارسال پست و فایل بدون نام به کانال \n"
              "🎵 پیدا کردن آهنگ از روی ویدیو \n"
              "📥 دانلود آهنگ از طریق لینک دانلود \n"
              "📥 دانلود ویدیو از تمام لینکها مثل یوتیوب اینستاگرام و غیره \n"
              "📥 دانلود ویدیو از طریق لینک اینستاگرام \n\n\n"
              "⚠️ برای شروع لطفا یه آهنگی/فیلمی بفرست: (می‌تونی فروارد کنی یا مستقیم آپلود کنی!)"
    },
    START_OVER_MESSAGE: {
        "en": "Send me a music and see how awesome I am!",
        "fa": "یه موزیک برام بفرست تا ببینی چقدر خفنم!",
    },
    HELP_MESSAGE: {
        "en": "It's simple! Just send or forward me an audio track, an MP3 file or a music. I'm waiting... 😁",
        "fa": "ساده س! یه فایل صوتی، یه MP3 یا یه موزیک برام بفرست. منتظرم... 😁",
    },
    ABOUT_MESSAGE: {
        "en": "This bot is created by @jojo.\n"
              "If you have any question or feedback feel free to message me on Telegram."
              " Or if you are a developer and have an idea to make this bot better, I appreciate your"
              " PRs.\n\n",
        "fa": "این ربات توسط @jojo نوشته شده است."
              " در دسترس است.\n\n"
              "اگر سوال یا بازخوردی دارید میتونید در تلگرام بهم پیام بدید. یا اگر برنامه نویس هستید و ایده "
              "ای برای بهتر کردن این ربات دارید، از PR هاتون استقبال میکنم."
    },
    DEFAULT_MESSAGE: {
        "en": "Send or forward me an audio track, an MP3 file or a music. I'm waiting... 😁",
        "fa": "یه فایل صوتی، یه MP3 یا یه موزیک برام بفرست... منتظرم... 😁",
    },
    ASK_WHICH_MODULE: {
        "en": "What do you want to do with this file?",
        "fa": "میخوای با این فایل چیکار کنی؟",
    },
    ASK_WHICH_TAG: {
        "en": "Which tag do you want to edit?",
        "fa": "چه تگی رو میخوای ویرایش کنی؟",
    },
    ASK_FOR_ALBUM: {
        "en": "Enter the name of the album:",
        "fa": "نام آلبوم را وارد کنید:",
    },
    ASK_FOR_ARTIST: {
        "en": "Enter the name of the artist:",
        "fa": "نام خواننده رو وارد کنید:",
    },
    ASK_FOR_TITLE: {
        "en": "Enter the title:",
        "fa": "عنوان رو وارد کنید:",
    },
    ASK_FOR_GENRE: {
        "en": "Enter the genre:",
        "fa": "ژانر رو وارد کنید:",
    },
    ASK_FOR_YEAR: {
        "en": "Enter the publish year:",
        "fa": "سال انتشار رو وارد کنید:",
    },
    ASK_FOR_ALBUM_ART: {
        "en": "Send me a photo:",
        "fa": "یک عکس برام بفرست:",
    },
    ASK_FOR_DISK_NUMBER: {
        "en": "Enter the disk number:",
        "fa": "شماره دیسک را وارد کنید:",
    },
    ASK_FOR_TRACK_NUMBER: {
        "en": "Enter the track number:",
        "fa": "شماره ترک را وارد کنید:",
    },
    ALBUM_ART_CHANGED: {
        "en": "Album art changed",
        "fa": "عکس آلبوم تغییر یافت.",
    },
    EXPECTED_NUMBER_MESSAGE: {
        "en": "You entered a string instead of a number. Although this is not a problem, "
              "I guess you entered this input by mistake.",
        "fa": "شما یک متن رو به جای عدد وارد کردید. اگر چه اشکالی نداره ولی حدس میزنم"
              " اشتباهی وارد کردی."},
    CLICK_PREVIEW_MESSAGE: {
        "en": "If you want to preview your changes click /preview.",
        "fa": "اگر میخوای تغییرات رو تا الان ببینی از دستور /preview استفاده کن.",
    },
    CLICK_DONE_MESSAGE: {
        "en": "Click /done to save your changes.",
        "fa": "روی /done کلیک کن تا تغییراتت ذخیره بشن.",
    },
    LANGUAGE_CHANGED: {
        "en": "Language has been changed. If you want to change the language later, use /language command.",
        "fa": "زبان تغییر یافت. اگر میخواهید زبان را مجددا تغییر دهید، از دستور /language استفاده کنید.",
    },
    MUSIC_LENGTH: {
        "en": "The file length is {}.",
        "fa": "طول کل فایل {} است.",
    },
    REPORT_BUG_MESSAGE: {
        "en": "That's my fault! Please send a bug report here: @amirhoseinsalimii",
        "fa": "این اشتباه منه! لطفا این باگ رو از اینجا گزارش کنید: @amirhoseinsalimii",
    },
    ERR_CREATING_USER_FOLDER: {
        "en": f"Error on starting... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"به مشکل خوردم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_DOWNLOAD_AUDIO_MESSAGE: {
        "en": f"Sorry, I couldn't download your audio... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم موزیکت رو دانلود کنم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_DOWNLOAD_PHOTO_MESSAGE: {
        "en": f"Sorry, I couldn't download your photo... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم عکست رو دانلود کنم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_DOWNLOAD_VIDEO_MESSAGE: {
        "en": f"Sorry, I couldn't download your video... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم ویدیوت رو دانلود کنم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_DOWNLOAD_LINK_MESSAGE: {
        "en": f"Sorry, I couldn't download your link... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم لینکت رو دانلود کنم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_TOO_LARGE_FILE: {
        "en": "This file is too big that I can process, sorry!",
        "fa": "این فایل بزرگتر از چیزی هست که من بتونم پردازش کنم، شرمنده!",
    },
    ERR_ON_READING_TAGS: {
        "en": f"Sorry, I couldn't read the tags of the file... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم تگ های فایل رو بخونم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_UPDATING_TAGS: {
        "en": f"Sorry, I couldn't update tags the tags of the file... {REPORT_BUG_MESSAGE_EN}",
        "fa": f"متاسفم، نتونستم تگ های فایل رو آپدیت کنم... {REPORT_BUG_MESSAGE_FA}",
    },
    ERR_ON_UPLOADING: {
        "en": "Sorry, due to network issues, I couldn't upload your file. Please try again.",
        "fa": "متاسفم. به دلیل اشکالات شبکه نتونستم فایل رو آپلود کنم. لطفا دوباره امتحان کن.",
    },
    ERR_NOT_IMPLEMENTED: {
        "en": "This feature has not been implemented yet. Sorry!",
        "fa": "این قابلیت هنوز پیاده سازی نشده. شرمنده!",
    },
    ERR_OUT_OF_RANGE: {
        "en": "The range you entered is out of the actual file duration. The file length is {}.",
        "fa": "بازه ای که انتخاب کردید خارج از طول کل فایل هست. طول کل فایل {} است.",
    },
    ERR_MALFORMED_RANGE: {
        "en": "You have entered a malformed pattern. Please try again. {}",
        "fa": "شما یک الگوی اشتباه وارد کردید. لطفا دوباره امتحان کنید. {}",
    },
    ERR_BEGINNING_POINT_IS_GREATER: {
        "en": "The ending point should be greater than starting point",
        "fa": "زمان پایان باید از زمان شروع بزرگتر باشد.",
    },
    BTN_TAG_EDITOR: {
        "en": "🎵 Tag Editor",
        "fa": "🎵 تغییر تگ ها",
    },
    BTN_MUSIC_TO_VOICE_CONVERTER: {
        "en": "🗣 Music to Voice Converter",
        "fa": "🗣 تبدیل به پیام صوتی",
    },
    BTN_MUSIC_CUTTER: {
        "en": "✂️ Music Cutter",
        "fa": "✂️ بریدن آهنگ",
    },
    BTN_BITRATE_CHANGER: {
        "en": "🎙 Bitrate Changer",
        "fa": "🎙 تغییر بیت ریت",
    },
    BTN_ARTIST: {
        "en": "🗣 Artist",
        "fa": "🗣 خواننده",
    },
    BTN_TITLE: {
        "en": "🎵 Title",
        "fa": "🎵 عنوان",
    },
    BTN_ALBUM: {
        "en": "🎼 Album",
        "fa": "🎼 آلبوم",
    },
    BTN_GENRE: {
        "en": "🎹 Genre",
        "fa": "🎹 ژانر",
    },
    BTN_YEAR: {
        "en": "📅 Year",
        "fa": "📅 سال",
    },
    BTN_CONVERT_VIDEO_TO_CIRCLE: {
        "en": "🎥 convert to circular video",
        "fa": "🎥 تبدیل به ویدیو دایره‌ای",
    },
    BTN_CONVERT_VIDEO_TO_GIF: {
        "en": "📷 convert video to gif",
        "fa": "📷 تبدیل ویدیو به گیف",
    },
    BTN_CONVERT_VOICE_TO_AUDIO: {
        "en": "🔊 convert voice to audio",
        "fa": "🔊 تبدیل صدا به موزیک",
    },
    BTN_ALBUM_ART: {
        "en": "🖼 Album Art",
        "fa": "🖼 عکس آلبوم",
    },
    BTN_DISK_NUMBER: {
        "en": "💿 Disk Number",
        "fa": "💿  شماره دیسک",
    },
    BTN_TRACK_NUMBER: {
        "en": "▶️ Track Number",
        "fa": "▶️ شماره ترک",
    },
    BTN_BACK: {
        "en": "🔙 Back",
        "fa": "🔙 بازگشت",
    },
    BTN_NEW_FILE: {
        "en": "🆕 New File or Link",
        "fa": "🆕 فایل یا لینک جدید",
    },
    MUSIC_CUTTER_HELP: {
        "en": "\n\nNow send me which part of the music you want to cut out?\n"
              "The file length is {}.\n\n"
              "Valid patterns are:\n"
              f"*mm:ss-mm:ss*:\n{EG_EN} 00:10-02:30\n"
              F"*ss-ss*:\n{EG_EN} 75-120\n\n"
              "- m = minute, s = second\n"
              "- Leading zeroes are optional\n"
              "- Extra spaces are ignored\n"
              "- Only English numbers are valid",
        "fa": "\n\nحالا بهم بگو کجای موزیک رو میخوای ببری؟\n"
              "طول فایل {} است.\n\n"
              "الگو های مجاز:\n"
              f"*mm:ss-mm:ss*:\n{EG_FA} 00:10-02:30\n"
              f"*ss-ss*:\n{EG_FA} 75-120\n\n"
              "- دقیقه: m، ثانیه s\n"
              "- صفرهای ابتدایی دل بخواه هستن\n"
              "- فاصله های اضافی در نظر گرفته نمیشن\n"
              "- تنها اعداد انگلیسی مجاز هستند",
    },
    DONE: {
        "en": "Done!",
        "fa": "انجام شد!",
    },
    OR: {
        "en": "or",
        "fa": "یا",
    },
    SEND_TO_CHANNEL: {
        "en": "🔊 send to channel",
        "fa": "🔊 ارسال به کانال",
    },
    SEND_TO_OTHERS: {
        "en": "🔊 send to others",
        "fa": "🔊 ارسال به دیگران",
    },
    SEND_TO_CHANNEL_MESSAGE: {
        "en": "1",
        "fa": "آیدی کانالتو با @ برام بفرست یا اگه خصوصیه و آیدی نداره، یکی از پست‌های متنی شو فروارد کن:"
    },
    SEND_TO_OTHERS_MESSAGE: {
        "en": "1",
        "fa": "آیدی کانالتو با @ برام بفرست یا اگه خصوصیه و آیدی نداره، یکی از پست‌های متنی شو فروارد کن:"
    },
    SEND_CHANNEL_NAME_WITH_ID: {
        "en": "You must send the channel ID in @ format: (like @telegram)",
        "fa": "آیدی کانال رو باید با فرمت @ بفرستی: (مثل @telegram)"
    },
    FIRST_ADMIN_ME : {
        "en": "First, admin me in this channel so that I can publish the post! 🥺",
        "fa": "اول منو تو این کانال ادمین کن تا بتونم پست رو منتشر کنم! 🥺",
    },
    CHANNEL_NOT_FOUND: {
        "en": "There is no such channel at all! Please enter a valid ID:",
        "fa": "همچین کانالی اصلا وجود نداره! لطفا یه آیدی درست وارد کن:"
    },
    NUMBER_OF_FILE_SENT: {
        "en": "Number of file sent: ",
        "fa":  "تعداد فایل های ارسال شده: ",
    }
}
