css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEhUTEhAVFhUSFRYVFRcRFxYVFxISFhgWGBkVFRcZHSggGBslHhUVIjEhJSkrLy4vFx8zODMsNygtLisBCgoKDg0OGxAQGy0lICYtLS0vLS0tLS0tLS0tLS0rLS0tLS0tLS0tLy0tLS0tLS0tLS0tLS0tLSstLS0tLS0tK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABAYDBQcCAQj/xABEEAABAwIDBAYGBwUHBQAAAAABAAIDBBEFITESQVFhBgcTcYGRIjJCUqGxFGJyksHR8CMzQ4LhJFNjc6KywhU0s9Lx/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAECBAUD/8QAJxEAAwACAQQCAQUBAQAAAAAAAAECAxExBBIhUTJBIhMzQmFxIxT/2gAMAwEAAhEDEQA/AO4oiIAiIgCIiAIiIAiIgCIvhcBqUB9RR31sY1kb5grGcUi98eR/JWUU+EV7l7JiKGMUi9/4H8l7ZXRHSRvibfNHFL6HcvZJRfGuB0IPcvqqWCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCItbXYs1mTPSd8B+atMOnpEVSlbZsHvAFyQBxOS11TjLG5NBcfIea0tRUvkN3Ov8h3BYVsjpUvkZqzv6J0+Kyu37I+r+ahveXaknvN15RaZiZ4R5Om+QiKNXYjDALzTRxjjI5rfmVbeipJRVmfp/hrNasH7DJH/FrSvkPWDhrzYVQH22StHm5qr+pHtFu2vRaGuI0Nu7JS4cTlb7V+Ts/jqtNh+MU9R+5qIpPsPa4+QN1NRzNc+Qm0b2nxtp9duzzGY/NbOKVrhdpBHJU9ZIZnMN2kg8vx4rPfSp/Hwes52uS3otTRYwDlJkeI0PfwW1BWO4qHpmiaVcH1ERULBERAEREAREQBERAEREAXl7w0XJsBqSkjw0Ek2A1KreI15lNhk0aDjzK9cWJ5GUu1KMuI4oX+iy4b8XfkFrURdKIULSMdU6e2EVex3ppRUZLXy7cg/hwjbffgdzT9ohVWr6xqqT/t6JrBudUOJPfsC3zKrWaJ5ZKx0zpagY1jEFHH2k8gY3Qb3PPusbq4rmEvSbFZNamOP/Kjaf8AcCtLiNJUVLxJPVGR4FgXN9UcAAQB4BeNdUtfieiwv7LDi3TWtrMqcfRYT7RsZXjv9n+X7y0LcKYXbUhdI86ulcXE9/HxWP6JUDSoB+00f1TtKpurGP8Asmx+P5LJV1T8s91KXBNZTMboxo7mhfX07Dqxp7wFCZi7QbSMdGfrC48/6KfHIHC7SCOIN1QsQ5cIhdnsbJGhYbEd25bLDsdxCjt2c/bxj+HUekbfVefSB8bcisaKZpzwQ0nydC6LdM6euPZ5xTjWKTU8dg+2PI8lZVw6tohJY3LXtsWvbk5rhmDcc1fegPS11TelqcqmMXDt07B7Q+sN/HXiBuw5+7xRmyYteUXRTaDEXRZHNvDh3KEi0VKpaZ5JtPaLfBM14Dmm4KyKq0NY6J1xodRx/qrNBMHtDmnI/qxXNy4Xjf8ARsx5FRkREXiegREQBERAEREARFrcarNhuyD6Tvg1WiXT0iKrtW2QMXrts7LT6Lf9R/Ja1F5keGglxAABJJyAAzJJ4LqxCidIw1Tp7Z4q6lkTHSSPDGMF3OcbBoHFcr6QdMKivJjpi6CmvYvGUsw7/ZbyHidyj9J8edikuy0ltJE70RoZ3j23cuA3DmcsDWgCwFgNLbgsebO34ng0Y8WvLI9JQxxeq3PicyfFSURZT2CIiAIiIDy9gcLEAjgc1r5cL2TtQvLHcNWnwWyRAa+lxE7XZzN2H7j7Lu4rYLDV0rZW7Lh3HeDxCh4fUOY7sZDmPUd77fzQGyUSua9hbPEdmWAh7COWoPEa5d43qWiA6v0fxVtZTxzs0kbcj3XjJzfAghbBc46qKzs5KmkJyBE8Y5Os14HL938V0ddXFfdKZiue16CmYbWmJ2fqnUcOYUNFapVLTKptPaLk03zG9fVpsCrP4ZPNvdvC3K5WSHFaZumu5bCIioWCIiAIiIDy9wAJOgFz3KqVU5keXHfpyG4LdY7PssDRq8/AfoKvrd0saXcZc9edBc36ysedM/6BC6wydUuHu6iL5E+A4q4dLccFDSyTZFwGzGD7UrvVHcNTyBXJcOgc1pc8kySkvkcdS5xub+Z8yp6nJpdqGGNvbJEUYaA1osBkF7RFhNIREQBERAEREAREQBQcWpi9m0314/SaRy1H64KciAwUVQJWNeN4z5EahZ1q6D9lNJFud6bPxH691bRAZujM/ZYpTO3TNfEfukj47K7CuIPk2Kikf7tTF5Fzb/ALt639K/xaM2deQiItR4HqN5aQRqDcK2U0we0OG8eXJVFbno/P6zD9ofI/gsvVRue70e2GtPRukRFzzWEREARF8cbC/BAVvGZtqU8G+j+fxKgr1I/aJJ3knzWCrqGxMfI71Y2ue7uaCT8l14XbKRgp7ezl/WFiH0mubTg3jpAHP4GZ4B+ALf8AUtaoOFPdIHzv9eeR0jvEnLzupy5mSu6mzZK0tBERULGGoqWsLQ4+udkf1+HmsymdD+iP/WJKhz3FsMLDFE4b6l2YdzDRmRv2mrVxCSGR9NUN2Z4DsuHvDc5p3ggg33ggqNrgnT1skIiKSAiIgCIiAIiIDWYx6Bjl9x1j9k/o+a2ai4nFtxPH1bjvGf4L7hsu3Ew/VAPeMvwQGLFTbsj7s0Z8iu7FcHxr1Wf5jPmu7lbek+zPn+giIthnCkUE2xI087HuORUdFWltaJT09lzRYqSTaY13FoPisq5DWvB0EERFACj177RvP1SpCh4uf2Tu4fMK0LdIrXDKwqt1m1nZYdNbWTZiHc9wDv8ATtK0qhdbz/2NKz36kE9zWOH/ACXTyvUMxwt0io00ewxrfdaB5BZERcs2hR5Y5Z5GUtONqac7Lfqt3ucdwABN+AK+VtX2YFgXPcdljG5l7jkAAMzmQusdWnQw0MZnqADVzj09D2LDY9k08chcjeANAq1Xai0z3MsfRjA46Cmjp4tIxm7e95zc88yfLIbloOsXoUMQYJYbMq4R+zdoJGi57J54Zmx3EncSrmizqmns1OU1o/OFNUEudHIwxzRktkY4WLXDXJSV1jpz0FixICRjuyqWD0JWj1gNGSges3nqO64PIKxs1HL2FbGYpB6rvYlHvMdoR+jY5LRNKjNcOTOiIrFAiIgCIiAWWtwE2Y5nuPc39fFbJa3DMpZ2/WB87oDLiYuYB71REPMrupXECzbqaNnGqiPgHtJ+F125bek4Zmz8oIiLYeAREQFlwV14m8rj4qctbgB/Zn7R+QWyXJyrVv8A03R8UERF5lwoeLj9k7w+YUxRsRbeJ/2T8M1aHqkVrhlVXO+ts/tKEbjJKfEdl+ZXRFz7rgGzHSSnRk5B7nNuf/H8F0s/7bMmP5IrKjVdXsEMa0vkeQGRsBLnOOgsM1grJKr6O+ojpZGwMteaRuyDtENGwD61yRmLrs/QXoRTUDRMD208jQTM8Z2cL2jGewPid53LlVSk3zDpms6uugRpiKusAdVOHoMyLaZp3DcX55kaZgbyehIomLYlFSwvnmfsxxDacfEAADeSSABvJCztts0pKUS0VA6P9bFJV1DYDFLF2jg2N8uwWuccg12yTsk6DUX3q/o01yFSfAUHGcHgrIzFURNkYdztWn3muGbTzBBU5FBJx/HOq6pprvw+Xto9ewnIDwODH5Nd47PiqdPWGF/Z1MMkEnuytIvzBtmOei/RGI18VNG6WaRrI2C7nO0A08SSQAN91XcL6V4ZixdTtc2U2J7OoiI22jUtDxY+Ga9ZyP7R41jnfhnIo5GuF2uBHEG69LpWKdU+HynaiEtO7jA/0fuvuAO6yr9T1T1jP3OIseNwnjLcubgXfJXWSSjx0iqot0/q9xhugpXd0jh82halnR3EnVn0G1O2bsu2PpEsEd7ZuAOd91lbuXsr2v0YybarVYbIHTzFpu07OY0Nh/8AV5NBK6WSGqc5r4XbL4tPG41HPgQb5raQxNYLNAAG4KSplwZm3iVE3g97vusJ/wCK7KuSdDGbWLR/4cEjvE3b/wAgutrf0q/Ay5vkERFqPEIiICwYAP2Z+0fkFs1AwRtohzJPxt+Cnrk5fm/9N2P4oIiLzLhfHtuCOIsvqICmubYkHdl5Kk9ZcYl+gQuF2TV0LXX3tN2keTyug4tFsyu+t6Q8dfjdUTrOpn/RWVEYu+jnjqAOIYbHwFwf5V08j7sW16MULtvTLn02w36TQVUIFy6F+wPrtG0wfea1ROrXEvpOGUr73LYhG77UV2Z/dB8VvMKxCOphjniN2SsD2nkRoeBGhHEFUjqx/stRiGHHIQT9tCP8CW1gOQGx4uXE/i0df+SZ0FaPpvgRxCilpmuDXPDSwnTbY4PaHW3Etse9bxFVPRZrfg4L0Y6r681UZqIhFFFI17n7bHbYY4OtGGkk3sMza1/Bd6RFNU65KxCngi4piMVLE+aeQMjjF3OdewFwNBmTcgWHFZ4ZWvaHNILXAOaRoWkXBHguddJw/F8TGGE7FNSBs9SL2dUE7JawDUt9MeZOoaujtaAAALACwA3AbgjWiU9sp3Wxgc9bQbFOC58crJdgaytaHtLRxPpBwG/Z42XL+rTorWOr4ZTTyxR079uR8rHRjIEbDdoDaJvaw3E3X6CRSraWitY03sIiKp6Bc/6H/wBpxnE6nVsIjpGHdlbbA7nRDzVyx3Em0lPNUO0hje+3EtBIaOZNh4qsdUWHOhw5skmclW99S8nV3aH0T4tDT/MrLhlH5aRU+uGjbFX0szRY1Eckb7e12RbYnnaQD+UKtLf9auJtqcRhhYbiiY4yEaCWTZJZ3gNZ5kbloF7x8UZ7+TNr1cs2sSmd7lNb7zo11Jcz6rm3rKw8I4h5k/8AqumLp9N+2Yc3yCIi0HkERZqOLbe1vE592p+ChvS2Slss1FHsxtHBo896zoi47e3s6C8BERQAiIgNTj8F2h/u5HuP9fmtBIwOBa4AhwIIOYIORBHBXKaMOaWnQiyqc8RY4tOoNv6rf0t7ntZlzTp7KJSw1uBvcaWM1VC5xcYLntacnUxnMked94vdx1tX05o3YrSV0DnN2mmmrI5WljmMJAa53smxNzY/wwukrUdJcAirYZI3sbtvaQyQtBcx+rSHa2uBcbxcKuTo5b3JaOppLTLsipvVfj7qmmME+VTRHsZg7UhuTH87gWJ4tJ3hXJchpp6Z05e1sIip/WHi9VQinq4fSp4pLVcYa0l0T7APBOY2c9LZubfK6JbeiW9LZJ6U9B6avkbM50sM7BsiWmfsPLdzXXBB1OevNbDoxgLaCIxNnmm2nl5dUv23XIAsDYWGWnMrYUFZHPGyWJ4eyRoc1zdCCsWMYrDSQunnkDI2C5J3nc1o3uO4BTt8EaXJMRVroJjdTXxPqJoRFFJIfozc9t0G5z887nQjXPdYmyqGtEp7WwiKFjWKxUcEk8ztlkbbniToGt4uJsAOJQFD63cUZIafDTM2MVL2yVD3uDRFTMN7knQktJHEx23qF0j6zW7H0bCmElrQzt3N2Y4mgWHZhwu4gaEi3IqiVD3V80lXUtu+Z201tzZkYya0cQBYeF96lMYGiwAAG4ZBaFC0tmZ5Ht6MFFS9mDclznEue52Ze45kknNSERXPM3nVaf7ZWjiyE/7vzXS1yrq+m7PE3t/vqc25ljmn5Ncuqro9M/8AmZM3yCIi0HkFt+j8FyX8Mh3nX8PNalrSTYanId6tdFB2bA3hrzO9ZupvU69nthndbM6Ii5xrCIiAIiIAtTjlJcdoNW+tzbx8Ftl8IurxbitorU9y0U1FNxSi7J1x6rtOXJQl1ZpUtowtNPTKb0po5qKobilG3aewbNVEP48GV3Ze0ABnyadxB6B0fxuCugbPTv2mO+8x29jxucFBVOrujE9JM6rwmQRSOzlp3/uZ/DRp14a5Fud8XVdL3flPJq6fqO38a4OoLxNE17Sx7Q5rgWua4XDmkWIIOoIVFwrrPg2hDiET6KfQiUExOPFrwNOZFuZV2oq6KdodDKyRp0dG5rwfFpXLcueToqlXBRT0Cq6N7nYTiBgjebmnqG9rECfcJBt5X5r3S9AZqmVs2LVv0rszdkDG7EDTxcMtrusL6G4yV/RT3sjsR8AtkN3BFgrK2KFpdLKyNo1dI5rAPFxVNxbrRo2O7OlElZMcgymaS2/N9sxzaHKFLfBLpLkulXVMhY6SR7WMYC5znGwa0byVwvpl0ndjEwDQW0cLrsByM79O0cOHAbhzJtYKzAMQxe78Rm7CMAmKmgzDHEei+U3IcRlx/lzCo8DJIJHUs7dmWHLk9m5zeIt+tVpWCoXdRmrMrekS0RFJQIiICOaz6LUU9Vuhks+3927J3wLvNduY8OAINwQCCNCDmCFxaaIPaWnQixVi6v8ApUINmhq3W2cqeR2TXM3RuO4jQeWtr6umyJPtZ45o35R0hEUmhpDK6w0HrHgPzW2qUrbMyW3om4HSXPaEZDJvM7yt6vMbA0AAWAyC9LlZLd1s3RPatBERULBERAEREAREQGOeEPaWuFwVWa6jdE6xzB0PH+qtSxzwteNlwuD+rhe2HK8b/o88mPuRUEUyvw90Rvq3ceHIqGulNKltGNpp6ZgraKKduxLGyRvCRocPiqvVdW9C523EJYHH2qeQtt3bVwPBW9FFRNcolU1wU0dBpW+pjGINHDtifxCHoNI718YxBw3jtiPndXJFT/z4/Rb9W/ZUKbq3oGu2pGyzu96okc4nv2bAqzUGHQ07dmGJkbeEbQ2/fbVSUV5iZ4RV03ywq50y6KMxBgIOxPH+6k4b9h9tWn4ajeDY0U1KpaZCbT2jhxlkhkMFUzs5W8fVeNzmnQg/rgpS6rjuBU9bH2c8YcB6pGT2HixwzHyO+653inQitpLmnd9JiHsOs2Vo+TvDyWDJ09Tx5RqjKnya5FBGKMDtiQOieNWytLSO++njZTI5Wuza4HuIPyWc9T0sNVSslbsvFx8R3LMvjnAZkgDnkgJGEdI6+hAa1wqYRoyYkPaODX6+d+4K/wCB9cNAxgZPT1FO72rtEjS7fZzfSP3QuWOxNhcGRh0sjsmsiBe5x4C2vhdXToz1XVlaRJXk00GR7FhHbSDg46MHfc8hqrO6a02VUpPaOr9GeltJiQeaV73iOwcTFKxocfZ2ntAJ32HLit4oeE4ZDSRNhgibHGwWa1oyHEneSdSTmSpioXCIiAIiIAiIgCIiAIiID44XyK09dg2+P7p/ArcorxkqHtFalVyU6RhabOBB4FeVbp6drxZzQe/d3HctVU4JvY7wd+a2x1Uv5eDNWFrg0yKRPRSM9Zh7xmPMKOtCpPg8mmuQiIrEBERAERZoaV7/AFWE893mobS5JS2QK/D4Z27M0LJBwkaHW7r6Kt1PVrh8p9GF7CdOye8eTTcfBdEp8EJ9d1uTcz5ra01IyP1W257z4rJlzY/Wz2jHf+HLqXqUp3Zvqqto3Na+O/n2eS2tF1NYWwgvbNMR/eyuz7wzZXQ0WJvbNKWjW4PgFLRi1NTRRA69m0An7TtT4rZIigkIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCxS0zHesxp7wPmsqKU9cAgvwmI+zbuJWM4LHxd5j8lskV1ltfbKdk+jWDBY+LvMfksjMIiHsk95Knon6t+2OyfRgjpI26MaPDPzWdEVG2+S+tBERQAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiAIiIAiIgCIiA//9k=">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
