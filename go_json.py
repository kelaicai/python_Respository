#encoding=utf-8
import json

js={"a":1,"b":2,
    "c":{"e":"h"},
    "f":[1,2,3,4,5],
    "h":[{"i":9,"l":2}]
}

def transform_json(js):
    if isinstance(js,dict):
#        print "js",js
        for k,v in js.items():
            if not isinstance(v,dict):
                print "k",k,v
            else:
                print k
                transform_json(v)

def pro_list(li,key):
    print "go list",li
    value = None
    for i in li:
        if isinstance(i,dict) and value==None:
            value = find_by_key(i,key)
        if isinstance(i,list) and value==None:
            value = pro_list(i,key)
        if value !=None:
            break
    return value
            

def find_by_key(js,key):
    print "ORI",js
    value=None
    print key in js,type(key)
    if isinstance(js,dict) and key not in js:
        for k,v in js.items():
            if isinstance(v,dict) and value==None:
                value=find_by_key(v,key)
            if isinstance(v,list) and value==None:
                value=pro_list(v,key)
            if value!=None:
                break
    else:
        print "go this",js
        if isinstance(js,dict) and key in js:
            value =js[key]
    return value



if __name__=="__main__":
    print find_by_key(js,"l")
