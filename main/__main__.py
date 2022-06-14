import json
import os

from main.bot import RelBot

ENV_JSON_NAME = "env.json"
ENV_JSON_PATH = os.path.join(os.getcwd(), ENV_JSON_NAME)


def main():
    env_json_file = open(ENV_JSON_PATH, encoding="utf-8") if os.path.exists(ENV_JSON_PATH) else None
    json_str = env_json_file.read()
    json_obj = json.loads(json_str)

    token = json_obj["bot_token"]
    guild_ids = json_obj["guilds"]

    env_json_file.close()

    extension_list = ["main.cogs.slash_commands_cog"]

    rel_bot = RelBot(extension_list, token, guild_ids)

    rel_bot.run()


if __name__ == "__main__":
    main()
