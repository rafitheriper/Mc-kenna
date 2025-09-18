# bot.py
import os
import discord
from discord.ext import commands
from discord import app_commands 

class McKennaBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

        # --- NEW: Error Handler ---
        # We are overriding the default error handler for the command tree.
        self.tree.on_error = self.on_app_command_error

    async def on_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        """A global error handler for all slash commands."""
        
        # Check if the error is the specific "Unknown Interaction" from autocomplete.
        # This happens when the user types faster than the bot can respond.
        if isinstance(error, app_commands.CommandInvokeError) and isinstance(error.original, discord.errors.NotFound):
            if error.original.code == 10062: # The specific error code for "Unknown Interaction"
                print("Ignoring a harmless 'Unknown Interaction' error from fast typing.")
                return # Just ignore it and do nothing.

        # If it's any other error, print it to the console as usual.
        # This ensures we don't accidentally ignore real bugs.
        print(f"An unhandled error occurred for command '{interaction.command.name}':")
        # You can import traceback and use traceback.print_exc() for a more detailed log if you want.
        raise error

    async def setup_hook(self):
        """This special function runs when the bot is setting up."""
        print("--- Loading Cogs ---")
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded Cog: {filename}")
                except Exception as e:
                    print(f"Failed to load cog {filename}: {e}")

        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

    async def on_ready(self):
        """This event runs when the bot is logged in and ready."""
        print("--------------------")
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")
        print("McKenna-Bot is ready to forge!")
        print("--------------------")