import json

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats_list.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    return cats_list

cats_info = get_cats_info("homework2_june23\cats.txt")
print(json.dumps(cats_info, indent=4, ensure_ascii=False))
