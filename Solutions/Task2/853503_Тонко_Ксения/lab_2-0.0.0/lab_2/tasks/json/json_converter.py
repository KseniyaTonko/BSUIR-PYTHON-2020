class JsonConverter:

    @staticmethod
    def to_json(obj):
        if isinstance(obj, (complex, bytes, bytearray, set, frozenset)):
            return "ERROR"
        if obj is None:
            return "null"
        if obj is False:
            return "false"
        if obj is True:
            return "true"
        if isinstance(obj, (int, float)):
            return str(obj)
        if isinstance(obj, str):
            result = ""
            chars = ["\"", "\n", "\t", "\\"]
            chars_json = ["\\\"", "\\n", "\\t", "\\\\"]
            for char in obj:
                if char in chars:
                    index = chars.index(char)
                    result = result + chars_json[index]
                else:
                    result = result + char
            return "\"" + result + "\""
        if isinstance(obj, (list, tuple)):
            answer = []
            for item in obj:
                answer.append(str(JsonConverter.to_json(item)))
            return "[" + ", ".join(answer) + "]"
        if isinstance(obj, dict):
            answer = []
            for key in obj:
                new_key = JsonConverter.to_json(key)
                if not isinstance(key, str):
                    new_key = "\"" + new_key + "\""
                answer.append(new_key + ": " + str(JsonConverter.to_json(obj[key])))
            return "{" + ", ".join(answer) + "}"
        return JsonConverter.to_json(obj.__dict__)

    @staticmethod
    def from_json(text):

        def is_float(string):
            try:
                float(string)
                return True
            except ValueError:
                return False

        def is_int(string):
            try:
                int(string)
                return True
            except ValueError:
                return False

        def find_list_or_dict(string, in_str_global, i, first_ch, second_ch):
            in_str = in_str_global
            j = i + 1
            balance = 1
            if not in_str:
                while j < len(string):
                    if string[j] == second_ch and balance == 1 and not in_str:
                        break
                    elif string[j] == second_ch and balance > 1:
                        balance -= 1
                    if j == len(string) - 1 and not in_str:
                        break
                    elif string[j] == "\"":
                        try:
                            end_index_1 = string[j+1:].index(", ")
                        except ValueError:
                            end_index_1 = -1
                        try:
                            end_index_2 = string[j+1:].index(": ")
                        except ValueError:
                            end_index_2 = -1
                        if end_index_1 == 0 or end_index_2 == 0:
                            in_str = False
                        elif in_str:
                            temp = temp + string[j]
                        else:
                            in_str = True
                    elif string[j] == first_ch:
                        balance += 1
                    j += 1
            return j

        def to_list(string):
            i = 0
            temp = ""
            answer = []
            in_str = False
            while i < len(string):
                if string[i] in [',', ']']:
                    if len(temp) > 0:
                        temp = JsonConverter.from_json(temp)
                        answer.append(temp)
                        temp = ""
                        in_str = False
                elif string[i] == ' ':
                    pass
                # случай вложенного списка:
                elif string[i] == '[' and not in_str:
                    j = find_list_or_dict(string, in_str, i, "[", "]")
                    answer.append(to_list(string[i+1:j+1]))
                    # in_str = False
                    i = j
                # случай вложенного словаря:
                elif string[i] == "{" and not in_str:
                    j = find_list_or_dict(string, in_str, i, "{", "}")
                    answer.append(to_dict(string[i+1:j+1]))
                    # in_str = False
                    i = j
                else:
                    if string[i] == "\"":
                        in_str = not in_str
                    temp = temp + string[i]
                i += 1
            return answer

        def to_dict(string):
            i = 0
            answer = {}
            temp = ""
            is_key = True
            in_str = False
            key = None
            while i < len(string):
                if i == len(string) - 1:
                    if len(temp) > 0:
                        temp = JsonConverter.from_json(temp)
                        answer[key] = temp
                        in_str = False
                elif string[i] in [" ", "}"]:
                    pass
                elif string[i] in ",":
                    if len(temp) > 0:
                        temp = JsonConverter.from_json(temp)
                        answer[key] = temp
                        in_str = False
                        temp = ""
                    is_key = True
                elif string[i] == "\"" and in_str:
                    if i == 0 or (i+2 < len(string) and string[i+2] != ":"):
                        in_str = False
                        if is_key:
                            temp = JsonConverter.from_json(temp + string[i])
                            key = temp
                        else:
                            answer[key] = temp
                        is_key = not is_key
                        temp = ""
                    else:
                        temp = temp + string[i]
                elif string[i] == ":":
                    if not in_str:
                        # print("OK OK OK OK OK", temp)
                        is_key = not is_key
                    else:
                        temp = temp + string[i]
                elif string[i] == "\"" and not in_str:
                    in_str = True
                    temp = "\""
                # случай вложенного словаря
                elif string[i] == "{":
                    # print(string)
                    j = find_list_or_dict(string, in_str, i, "{", "}")
                    answer[key] = to_dict(string[i+1:j+1])
                    in_str = False
                    i = j
                # случай вложенного списка
                elif string[i] == "[":
                    j = find_list_or_dict(string, in_str, i, "[", "]")
                    answer[key] = to_list(string[i+1:j+1])
                    # in_str = False
                    is_key = not is_key
                    i = j
                else:
                    temp = temp + string[i]
                i += 1
            return answer

        if text == "null":
            return None
        if text == "false":
            return False
        if text == "true":
            return True
        if text[0] == text[-1] == "\"":
            result = ""
            latest_char = -80
            chars = ["\"", "\n", "\t", "\\"]
            chars_json = ["\"", "n", "t", "\\"]
            i = 1
            while i < len(text)-2:
                if text[i] == "\\" and text[i+1] in chars_json:
                    index = chars_json.index(text[i+1])
                    result = result + chars[index]
                    latest_char = i + 1
                    i += 1
                else:
                    result = result + text[i]
                i += 1
            if latest_char < len(text) - 3 and len(text) >= 2:
                result = result + text[-2]
            return result
        if is_int(text):
            return int(text)
        if is_float(text):
            return float(text)
        if text[0] == "[":
            return to_list(text[1:])
        else:
            return to_dict(text[1:])
