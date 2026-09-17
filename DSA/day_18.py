def find_new_errors():
    errors = (["500","404", "403"], ["404", "500"])
    today_list, yesterday_list = errors

    print(set(today_list)-set(yesterday_list))

find_new_errors()