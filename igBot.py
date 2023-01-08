import instaloader

L = instaloader.Instaloader()

USER = ""       #Type here the profile username you want to use as a bot
PROFILE = ""    #Type here the profile username you want to check its following list

# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

print("Fetching followers of profile {}".format(profile.username))
followers = set(profile.get_followers())
following = set(profile.get_followees())

notFollowingBack = following - followers
print("Storing not following back users into file.")

with open("notFollowingBack.txt", 'w') as f:
    print("List of Instagram profiles not following you (that you still follow):", file=f)
    for flw in notFollowingBack:
        print(flw.username, file=f)