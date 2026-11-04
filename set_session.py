from instagrapi import Client

SESSION_ID = "1266358206:fLo5ZH87aNPulC:6:AYI1x-mNgRg60HJvIE8DWXgG4YAPFBvPh1TvYt9QSg"
USER_ID = "1266358206"

cl = Client()
cl.set_settings({
    "user_id": USER_ID,
    "authorization_data": {
        "sessionid": SESSION_ID,
        "ds_user_id": USER_ID
    }
})

cl.dump_settings("session.json")
print("session.json successfully rebuilt with complete authentication data!")
