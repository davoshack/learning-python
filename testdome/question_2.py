import io

def get_occurrence_count(to_search, stream):
    """
    :param to_search: (String) The text to search for
    :param stream: (StringIO) An in-memory stream for text I/O
    :returns: (int) The number of lines that contain to_search
    """
    stream.seek(0)
    lines = stream.readlines()
    num_lines = 0
    for line in lines:
        if to_search in line:
            num_lines += 1

    return num_lines


    
    return None

if __name__ == "__main__":
    stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")
    print(get_occurrence_count('good', stream))
    stream.close()