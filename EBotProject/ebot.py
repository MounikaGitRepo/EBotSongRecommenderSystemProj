from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import random
import recommend as r


tone=" "
def get_resp(user):
   d=dict()
   greet= ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", 
    "good morning", "morning", "good day", "good afternoon", "good evening", 
    "greetings", "greeting","g’day", "howdy","what's up"]
   botgreet=[
            "How are you today?",
            "How are you feeling?",
            "What's up?",
            "Greetings human, are you well?",
            "How are things going?",
            "How do you do?"
    ]
   greet_rep=["good","better","amazing","great","peaceful","fine","angry","depressed","cheerful","nervous",
        "lonely","excited","lost","loser","winner","optimistic","fun","sad","scary","joyful","joyous",
        "lazy","lively","jovial","upset","well","notwell","relaxed","stressful","regrateful","restful",
        "confident","calm","mysterious","nothing","boring","mad","crazy","worse","waste","joy","sucks","bored","happy","scared"

]
   last=["bye","goodbye","byebye","see you"]
   wel=["your welcome","welcome","your most welcome","my pleasure","dont mention"]
   tu=["thank you","thanks","thanks alot","thankyou"]


   
   global tone
   li=list(user.split(" "))
   if "recommend" in li:
      d=r.recommendsongs(tone)
      return d
   if "how are you" in user:
      str2="I'm fine, thank you for asking"
      d["txt"]=str2
      d["tone"]=tone
      d["rec"]=0
      return d

   for i in greet:
      if i in li:
       str2="Hi  I am EntertainmentBot,"+" "+random.choice(botgreet)
       d["txt"]=str2
       d["tone"]=tone
       d["rec"]=0
       return d
   for j in greet_rep:
      if j in li:
         apikeys='Vm9fFAt5OFlxWBj433ouRal3BwKYfhFEa3igk4Qb0Vdm'
         url='https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/7a58e5a6-ac69-45b2-a526-8061cc4dc8cd'
         authenticator=IAMAuthenticator(apikeys)
         ta=ToneAnalyzerV3(version="2017-09-21",authenticator=authenticator)
         ta.set_service_url(url)
         res=ta.tone(user).get_result()
         tone=res['document_tone']['tones'][0]["tone_name"]

         
         if tone=="Joy":
            str2="""I am happy that you are happy :), How can i help you?
            """
            d["txt"]=str2
            d["tone"]=tone
            d["rec"]=0
            return d
         elif tone=="Anger":
            str2="""Sorry to hear that :(, How can i help you?"""
            d["txt"]=str2
            d["tone"]=tone
            d["rec"]=0
            return d
         elif tone=="Sadness":
            str2="""Its ok now tell me, How may i help you?"""
            d["txt"]=str2
            d["tone"]=tone
            d["rec"]=0
            return d
         elif tone=='Fear':
            str2="Don't worry i am there with you, How may i help you?"
            d["txt"]=str2
            d["tone"]=tone
            d["rec"]=0
            return d
         else:
            str2="Oh i see :|, How can i help you?"
            d["txt"]=str2
            d["tone"]=tone
            d["rec"]=0
            return d


   for k in last:
      if k in li:
         str2="Have a great day byee :)"
         d["txt"]=str2
         d["tone"]=tone
         d["rec"]=0
         return d
   for l in wel:
      if l in user:
         str2="Anything else you would like me to do please let me know :)"
         d["txt"]=str2
         d["tone"]=tone
         d["rec"]=0
         return d
   for m in tu:
      if m in user:
         str2="Happy to help :)"
         d["txt"]=str2
         d["tone"]=tone
         d["rec"]=0
         return d


   
        
        
         
        
      
     

            

