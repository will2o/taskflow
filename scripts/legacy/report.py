# Script historique de reporting. NE PAS MODIFIER : il est remplacé au Module 2 (TP refactoring).
# Volontairement non conforme aux conventions du projet.
import json,sys,urllib.request
def main():
    u="http://localhost:8000/tasks"
    d=json.loads(urllib.request.urlopen(u).read())
    c={}
    for t in d:
        s=t["status"]
        if s in c: c[s]=c[s]+1
        else: c[s]=1
    for k in c: print(k+": "+str(c[k]))
    tot=0
    for k in c: tot=tot+c[k]
    print("total: "+str(tot))
    if len(sys.argv)>1 and sys.argv[1]=="--json": print(json.dumps(c))
if __name__=="__main__": main()
