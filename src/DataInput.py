import json

from src import client
from src.Pokemon import Pokemon
from src.Agent import Agent


def loadAllPokemons(pokemons):
    pokLst = []
    jsonTemp = json.loads(pokemons)
    for i in range(len(jsonTemp['Pokemons'])):
        pokLst.append(Pokemon(jsonStr=jsonTemp['Pokemons'][i]))
    return pokLst


def loadAllAgents(agents):
    agentLst = []
    jsonTemp = json.loads(agents)
    for i in range(len(jsonTemp['Agents'])):
        agentLst.append(Agent(jsonStr=jsonTemp['Agent'][i]))
    return agentLst
