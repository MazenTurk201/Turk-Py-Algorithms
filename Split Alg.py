text = "hi im mazen sameh. i live in maadi."
def splitt(textt,custm=None):
    num = 0
    if custm is None:
        for i in textt:
            if i == " ":
                num += 1
        if textt[-1] == " ":
            num -= 1
    elif custm is not None:
        for i in textt:
            if i == custm:
                num += 1
    print(num)
splitt(text)
splitt(text,".")
splitt(text,",")