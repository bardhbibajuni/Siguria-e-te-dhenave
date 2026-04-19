def decrypt(encrypted_message, lines):
    result = []

    for item in encrypted_message:
        if item == "NOT FOUND":
            result.append("NOT FOUND")
        else:
            line_num, word_index = item

            if 0 <= line_num < len(lines):
                words = lines[line_num].split()

                if 0 <= word_index < len(words):
                    result.append(words[word_index])
                else:
                    result.append("NOT FOUND")
            else:
                result.append("NOT FOUND")

    return " ".join(result)