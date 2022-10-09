def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
       #Check if the actual character and the previous one match
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char #Add the char and the total count to our sequence
            count = 1 #Reset the count
            prev_char = char #Reset our new char
        else:
            #If char match, just increment the value
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding

input = str(input("Introdueix els bytes que vols convertir\n"))
print("Resultat del run-length encoder: ", rle_encode(input))
