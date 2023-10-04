import json

def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    
    if required_fields is None:
        required_fields = []
    if keywords is None:
        keywords = []

    try:
        json_doc  = json.loads(json_str)
    except json.JSONDecodeError:
        print("JSON Decode Error")
        return
    
    for field, value in json_doc.items():
        if field in required_fields:
            for keyword in keywords:
                if keyword.lower() in value.lower():
                    keyword_callback(field, keyword)

def keyword_callback(field, keyword):
    print(f"Keyword '{keyword}' in field '{field}'")


json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields = ["key1"]
keywords = ["word2"]

parse_json(json_str, required_fields, keywords, keyword_callback)