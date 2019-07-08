env = {
    "BOT_TOKEN" : "897254025:AAHsm0feiMTA_7azdg2bb1Tc3nsEOFDtOvE",
    "BOT_NAME" : "dev1010_bot"
}

def get_property(property_name):
    return env.get(property_name,None)

def properties():
    return list(env.keys())