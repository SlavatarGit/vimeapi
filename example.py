import vimeapi

# Vars
vimeapi.DEV_TOKEN = "ur token here"

# About
print(vimeapi.DEV_TOKEN)
print(vimeapi.DEV_API)

# Examples
print(vimeapi.online_staff())

print(vimeapi.user_name("SlavatarAgent"))
print(vimeapi.request_limit())