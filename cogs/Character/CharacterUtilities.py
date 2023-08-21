# from discord.ext import commands
# from discord import app_commands, Embed, Interaction
# from discord import SlashCommandGroup
import asyncio
import json
import os 


class characterUtils():
    async def get_characters(self):
        try:
            print("get_characters called")
            os.chdir('../Character')
            print(os.getcwd())
            with open('characters.json', 'r') as f:
                characters = json.load(f)
                print('characters loaded')
                return characters
        except Exception as e:
            print(f'Error: {e}')
            return {}
    
    async def save_characters(self, file):
        print('saving...')
        with open('characters.json', 'w') as f:
            json.dump(file, f)
            print('characters.json saved')

    async def get_tracks(self):
        os.chdir('../Character')
        print(os.getcwd())
        with open('tracks.json', 'r') as f:
            tracks = json.load(f)
            return tracks

    async def get_races(self):
        os.chdir('../Character')
        print(os.getcwd())
        with open('races.json', 'r') as f:
            races = json.load(f)
            return races
    
    async def get_feats(self):
        os.chdir('../Character')
        print(os.getcwd())
        with open('feats.json', 'r') as f:
            feats = json.load(f)
            return feats