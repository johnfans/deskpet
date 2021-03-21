import json
def conf():
    c=1
    db=[]
    while True:
        try:
            with open(str(c)+'.json') as fobj:
                conf=json.load(fobj)
        except FileNotFoundError:
            break
        else:
            db.append(conf)
            c=c+1
    return db
if __name__=='__main__':
    db=conf()
    print(db)