from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
ADMINS = [
    env.str('ADMIN_ID')
]
