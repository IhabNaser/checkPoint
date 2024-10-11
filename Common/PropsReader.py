from jproperties import Properties

props_configs = Properties()
expected_configs = Properties()

# app-properties
with open('../Properties/app-props.properties', 'rb') as config_file:
    props_configs.load(config_file)

webUrl = props_configs.get("webUrl").data
userSetter = props_configs.get("userSetter").data
passwordSetter = props_configs.get("passwordSetter").data
buttonSetter = props_configs.get("buttonSetter").data
navigationSetter = props_configs.get("navigationSetter").data
screenshotsPath = props_configs.get("screenshotsPath").data
userLine = props_configs.get("userLine").data
phoneLine = props_configs.get("phoneLine").data
passLine = props_configs.get("passLine").data
first_name = props_configs.get("first_name").data
last_name = props_configs.get("last_name").data
Day = props_configs.get("Day").data
Month = props_configs.get("Month").data
Year = props_configs.get("Year").data
Gender = props_configs.get("Gender").data
input_name = props_configs.get("input_name").data
input_last_name = props_configs.get("input_last_name").data
enter_name = props_configs.get("enter_name").data
create_account = props_configs.get("Create account").data
Tab = props_configs.get("Tab").data
input_day = props_configs.get("input_day").data
input_month = props_configs.get("input_month").data
input_year = props_configs.get("input_year").data
enter_birthday_gender = props_configs.get("enter_birthday_gender").data
link = props_configs.get("link").data
personal_use = props_configs.get("personal_use").data
own_gmail_address = props_configs.get("own_gmail_address").data
create_gmail_adress = props_configs.get("create_gmail_adress").data
random_input_mail = props_configs.get("random_input_mail").data
strong_password = props_configs.get("strong_password").data
english_lang = props_configs.get("english_lang").data
hebrew_lang = props_configs.get("hebrew_lang").data
arabic_lang = props_configs.get("arabic_lang").data
next_create = props_configs.get("next_create").data
wrong_pass = props_configs.get("wrong_pass").data
control_meta = props_configs.get("control_meta").data
wrong_pass_try_again = props_configs.get("wrong_pass_try_again").data
random_user = props_configs.get("random_user").data
option = props_configs.get("option").data

# Expected Results - Comparison
with open('../Properties/expectedProps.properties', 'rb') as config_file:
    expected_configs.load(config_file)

button = expected_configs.get("button").data
Forgot_email = expected_configs.get("Forgot_email").data
input_name = expected_configs.get("input_name").data
next = expected_configs.get("next").data
enter_birthday_gender = props_configs.get("enter_birthday_gender").data
enter_phone_recovery = props_configs.get("enter_phone_recovery").data
main_Page_Title = props_configs.get("main_Page_Title").data
learn_more = props_configs.get("learn_more").data
google_help = props_configs.get("google_help").data
chrome_guest = props_configs.get("chrome_guest").data
heading = props_configs.get("heading").data
form = props_configs.get("form").data
wrong_pass_try_again = props_configs.get("wrong_pass_try_again").data
enter_email_phone = props_configs.get("enter_email_phone").data
section = props_configs.get("section").data
div = props_configs.get("div").data
enter_password = props_configs.get("enter_password").data
cant_find_account = props_configs.get("cant_find_account").data
expected_ar_lang = props_configs.get("expected_ar_lang").data
login_ar = props_configs.get("login_ar").data
fogot_mail_ar = props_configs.get("fogot_mail_ar").data
login_he = props_configs.get("login_he").data
heb_lang = props_configs.get("heb_lang").data
heb_lang_email_phone = props_configs.get("heb_lang_email_phone").data
