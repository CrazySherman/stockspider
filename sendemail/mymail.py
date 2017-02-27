from email.MIMEMultipart import MIMEMultipart
import smtplib
import json

def sendout_email(stock_name):
    with open('sendemail/pem.json') as config_file:
        config = json.load(config_file)

        fromaddr = config["fromaddr"]
        toaddr = config["toaddr"]
        server = smtplib.SMTP(config["hostname"], 587)
        # server.starttls()

        server.login(config["login"], config["passwd"])
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "NEW FINANCIALS RELEASED FOR " + stock_name    
        
        body = ""
        text = msg.as_string() 
        print text
        server.sendmail(fromaddr, toaddr, text)
        server.quit()