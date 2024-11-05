import pickle

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    w = ""
    result = []
    
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            if w in dictionary:
                result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    
    if w:
        result.append(dictionary[w])
    return result

def decompress(compressed):
    """Decompress a list of output ks to a string."""
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    result = []

    w = chr(compressed.pop(0))
    result.append(w)

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            continue

        result.append(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry

    return "".join(result)

def save_compressed_to_file(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_compressed_from_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    # Read "Alice in Wonderland" text file
    with open("Alice's Adventures in Wonderland.txt", "r", encoding="utf-8") as f:
        text = f.read()
    
    # Compress the text
    compressed = compress(text)
    print("Compression completed.")
    
    # Save the compressed data to a file
    save_compressed_to_file(compressed, "compressed_data.pkl")
    print("Compressed data saved to file.")
    
    # Load the compressed data from the file
    loaded_compressed = load_compressed_from_file("compressed_data.pkl")
    print("Compressed data loaded from file.")
    
    # Decompress the loaded data
    decompressed = decompress(loaded_compressed)
    print("Decompression completed.")
    
    # Print the first 45 characters of the decompressed text
    print("First 45 characters of decompressed text:", decompressed[:45])

if __name__ == "__main__":
    main()
