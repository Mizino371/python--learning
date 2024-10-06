veta = input("Napíš vetu: ")
if veta[-1] == ("."):
    print("Ide o oznamovaciu vetu")
elif veta[-1]==("!"):
    print("Ide o rozkakozvaciu vetu")
elif veta[-1] == ("?"):
    print("Ide o opytovaciu vetu")
else:
    print("zle zakončenie vety")