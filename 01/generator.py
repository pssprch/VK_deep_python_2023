def search_file(file_name_or_obj, srch_words):
    srch_words = [word.lower() for word in srch_words]
    if isinstance(file_name_or_obj, str):
        file_obj = open(file_name_or_obj, 'r')
    else:
        file_obj = file_name_or_obj

    try:
        for ln in file_obj:
            words = ln.strip().split()
            for word in words:
                if word.lower() in srch_words:
                    yield ln.strip()
                    break
    finally:
        if isinstance(file_name_or_obj, str):
            file_obj.close()
