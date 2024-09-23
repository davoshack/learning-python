import io

def count_hobby(hobbies, word):
    count = 0
    for hobby in hobbies:
        if word in hobby.split():
            count += 1

    
    return count

if __name__ == "__main__":
    print(count_hobby('Tennis', 'Table Tennis'))