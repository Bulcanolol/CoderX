import colorama;
from colorama import Fore;
import os;
import openai;
os.system("cls")
print(Fore.GREEN + """
 ██████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██║     ██║   ██║██║  ██║█████╗  ██████╔╝ ╚███╔╝ """ + Fore.CYAN + """
██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗ ██╔██╗ 
╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║██╔╝ ██╗
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""+ Fore.WHITE)

apikey = ""

if os.stat('./stuff/apikey.coderxlogin').st_size == 0:
    login_key_question = input(Fore.CYAN + "Key login " + Fore.YELLOW + "(From OpenAI API) " + Fore.GREEN + "> ")
    print(Fore.WHITE)
    key_file_setup = open("./stuff/apikey.coderxlogin", "w")
    key_file_setup.write(login_key_question)
    key_file_setup.close()
    print(Fore.WHITE)
    apikey = login_key_question

    key_file_setup = open("./stuff/logs.log", "w")
    key_file_setup.writelines("[REGISTER] User registered")
    key_file_setup.close()
else:
        key_file =  open('./stuff/apikey.coderxlogin', "r")
        

        apikey = key_file.readlines(1)[0]
        key_file_setup = open("./stuff/logs.log", "w")
        key_file_setup.writelines("[LOGIN] User log on")
        key_file_setup.close()

question_language = input(Fore.CYAN + "Language " + Fore.YELLOW + "(Example: js, py, php. Write file extension) " + Fore.GREEN + "> ")
print(Fore.WHITE)
languages = ["py", "js", "java", "c", "cpp", "cs", "go", "swift", "php", "html", 
"css", "scss", "sass", "less", "sql","ruby","kotlin","rust","dart","bash","bat","vbs","ts","hx"]
if(question_language == "delete_login_key"):
       key_file_setup = open("./stuff/apikey.coderxlogin", "w")
       key_file_setup.write("")
       print(Fore.RED + "[!] The key has been successfully deleted")
       print(Fore.WHITE)
       key_file_setup.close()
       exit()
if(question_language == "ai_info"):
       print("AI from OpenAI: https://openai.com/")
       exit()
if(question_language == "working_extensions"):
       print(languages)
       exit()
if not languages.__contains__(question_language):
       print(Fore.RED + "[!] Unrecognized extension"+ Fore.WHITE)
       exit()
question = input(Fore.CYAN + "Explain code " + Fore.YELLOW + "(Expose yourself accurately!) " + Fore.GREEN + "> ")
if(not question):
       print(Fore.RED+ "[!] Please, ask something" + Fore.WHITE)
       exit()
print(Fore.WHITE)

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write me only a code in " + question_language + " to " + question + "and add on the top a comment writed 'Generated with CoderX'",
  temperature=0,
  max_tokens=3521,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

new_file = open("./code-gen/auto-gen-code." + question_language, "w")
new_file.write(response.choices[0].text)

print(Fore.WHITE)