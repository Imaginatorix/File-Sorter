import re, os, time

time_to_stop = "16:00"
for i in range(len(time_to_stop)):
    if time_to_stop[i] == ":":
        stop_hour = int(time_to_stop[0:i])
        stop_minute = int(time_to_stop[i + 1:len(time_to_stop)])

requirements_path = "C:\\Users\\pcdum\\Desktop\\School"
os.chdir(requirements_path)

TAGS = {
    "Subject": ["Biology", "Physics", "Chemistry"],
    "Assessment Type": ["LQ", "QE", "Quiz"]
}

order_heirarchy = ["Subject", "Assessment Type"]

def identify_tag(tag, word):
    pattern = r"\b(%s)\b" % tag
    tags = re.findall(pattern, word)

    if len(tags) > 0:
        return True
    else:
        return False

word = "Activity VEt 1"

t = time.time()
current_hour = time.strftime('%H', time.localtime(t))
current_minute = time.strftime('%M', time.localtime(t))

print (os.listdir())
print (int(current_hour) < stop_hour and int(current_minute) < stop_minute)

while int(current_hour) < stop_hour:
    if int(current_minute) < stop_minute:
        break

    depth = 0
    for tag_type in order_heirarchy:
        for f in os.listdir():
            full_file = os.path.join(os.getcwd(), f)
            if os.path.isfile(full_file):
                for tag in TAGS[tag_type]:
                    if identify_tag(tag, f):
                        if not os.path.exists(tag):
                            os.mkdir(tag)
                        os.chdir(tag)
                        depth += 1
                        os.rename(full_file, os.path.join(os.getcwd(), f))

    for _ in range(depth):
        os.chdir("..")

    time.sleep(60)
    t = time.time()
    current_hour = time.strftime('%H', time.localtime(t))
    current_minute = time.strftime('%M', time.localtime(t))




