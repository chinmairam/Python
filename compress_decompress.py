def decompress(input):
    
    # Number of characters in the input
    length = len(input)
    
    # Initialize an index for the character position
    index = 0
    
    # Define an inner decompression function
    def decompress_inner(input, index, length):
        
        # Initialize the number
        number = ''
        
        # Initialize the output
        output = ''
        
        # Loop over the characters of the input (with a while loop)
        while index < length:
            
            # If the current character is a digit
            if input[index].isdigit():
                
                # Update the number
                number = number + input[index]
                
                # Update the index
                index = index+1
                
            # If the current character is an open bracket
            elif input[index] == '[':
                
                # Update the index
                index = index+1
                # Call the inner decompression function recursively on the same input, 
                # and get the inner output and the updated index
                output_inner, index = decompress_inner(input, index, length)
                
                # Translate the number from a string to an integer
                number = int(number)
                
                # Repeat the inner output number times and add it to the outer output
                output = output + number*output_inner
                
                # Re-initialize the number
                number = ''
                
            # If the current character is a letter
            elif input[index].isalpha():
                
                # Update the output
                output = output + input[index]
                
                # Update the index
                index = index+1

            # If the current character is a closed bracket
            elif input[index] == ']':
                
                # Update the index
                index = index+1
                
                # Return the output and the index
                return output, index
                
        return output, index
        
    # Call the inner decompression function
    output, index = decompress_inner(input, index, length)
    
    # Return the final output
    return output

print(decompress('3[abc]4[ab]c'))
