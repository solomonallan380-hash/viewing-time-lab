def clean_data(data):
    
    cleaned_list = []
    removed_count = 0

    for value in data:
        value = value.strip()

        if value == "" or value == "minutes":
            removed_count += 1
            continue

        try:
            cleaned_list.append(float(value))
        except ValueError:
            removed_count += 1

    return cleaned_list, removed_count

  
