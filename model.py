from pydantic import BaseModel
from typing import List
import openai
import random
import numpy as np

# classe de mensagens do role: user
class Message(BaseModel):
    username: str
    content: str

# classe de mensagens do estilo gpt, o content é obtido pelo Message.content
class GptMessage(BaseModel):
    role: str
    content: str

#todo: implementar a logica de achar uma cidade mais apropriadamente
class City:
    name:str

    def __init__(self, name):
        self.name = name

# classe que vai ter as informações de um lugar
class Place:
    country: str
    state: str
    city : City

    def __init__(self, country, state, city):
        self.country = country
        self.state = state
        self.city = city

    # checando se o lugar existe no banco de dados
    def find(self, country, state, city) -> bool:
        if country not in database_lugares.values():
            return False
        
        if state not in database_lugares[country].values():
            return False
        
        return True

def answerDummy(*args, **kwargs):
    buzzwords = [ "Dev Software", "Concepcao de artefatos", "????", "Forms", "Eigenvalues "
    "synergy", "pivot", ",", "mas também", "blockchain", ", além de ", "cloud-native", ".",
    "big data",]
    return " ".join(random.sample(buzzwords, 3) )


class OpenaiInteface:
    """Essa classe proverá (quando isso for implementado) 
    as respostas de um chatbot.
    Essa classe deve preparar os parametros, prompts e outras coisas
    Parameters:
    useDummy (bool): usar um chatbot fake ou não;."""
    def __init__(self, useDummy=True, **kwargs):
        self.openai = None
        self.getReply = answerDummy
        if (useDummy):
            #nao usar o chatgpt de verdade
            self.openai = None
        else:
            #inicializar o modulo openai
            #implementar aqui
            pass

# classe de usuario
class User():
    username: str
    message_history: List[GptMessage]
    
    def __init__(self, username="John Doe", message_history=[]):
        self.username = username
        self.message_history = message_history

    # adiciona mensagem comm base na role
    def addMessage(self, msg: Message):
        role = "assistant"

        if msg.username != "assistant":
            role = "user"

        self.message_history.append(GptMessage(role=role, content=msg.content))
    
    # retorna cada mensagem do historico no formato de Message
    def getMessageHistory(self) -> List[Message]:
        return [Message(username=item.role, content=item.content) for item in self.message_history]

# banco de dados de usuarios (provisorio)
user_list = {"André" : User(username="André", message_history=[GptMessage(role="user", content="Se estou lendo isso, é porque deu certo")])}

# banco de dados de lugares (provisorio)
database_lugares = {"País1" : {"Estado1" : np.array(['Cidade1'])}}

#exemplo#
rob = User(username="Robinson", message_history=[])
rob.addMessage(Message(username="robinser", content="eae"))
#print(rob.message_history)