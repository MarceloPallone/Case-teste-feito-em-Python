import pyautogui
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#Para funcionar esse codigo e necessario ser salvo na area de trabalho com o nome da pasta sendo "case" e utilizar  o outlook.

pyautogui.alert("O PDF vai ser gerado e  enviado por e-mail,Porfavor espere o término do programa sem mexer no mouse ou teclado.")
pyautogui.PAUSE = 2.0

#criar pdf e salvar o pdf
cnv=canvas.Canvas("caseTest.pdf")
cnv.drawString(50 , 50, "Este arquivo PDF foi feito utilizando o Reportlab e a automatização do processo foi utilizado Python")
cnv.save()


#abrindo o navegador e o e-mail 
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://outlook.live.com/mail/0/')
pyautogui.press('enter')
time.sleep(5)

#montando o e-mail 
pyautogui.click(x=220, y=180)
time.sleep(3)
pyautogui.write('rh@dnaconsult.com.br')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Case para estagio feito em Python.')
pyautogui.press('tab')
pyautogui.write('Boa tarde! segue em anexo o codigo e o PDF gerado pelo mesmo.')
pyautogui.press('enter')
pyautogui.write('Muito obrigado pela oportunidade!')

#anexando arquivos no e-mail
pyautogui.hotkey('win','d')
pyautogui.write('case')
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(x=230, y=180)
pyautogui.hotkey('ctrl','a')
pyautogui.mouseDown()
time.sleep(3)
pyautogui.moveTo(x=500, y=600)
pyautogui.hotkey('alt','tab')
pyautogui.mouseUp()
pyautogui.moveTo(x=450, y=860)
pyautogui.click()


pyautogui.alert("O PDF foi criado e enviado por e-mail,aperte enter para finalizar e cheque seus e-mails enviados!")




