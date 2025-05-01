def file_processor():
    #Get input filename from user
    input_filename=input("Enter the name of the file to read:")

    try:
        #ty to pen and read the file
        with open(input_filename, 'r')as input_file:
            content = input_file.read()
            #process the content(example:convert to uppercase)
            modified_content =content.upper()
            #create output filename
            output_filename= f"modified_{input_filename}"
            #write modified content to new file 
            with open (output_filename,'w')as output_file:
                output_file.write(modified_content)
                print(f"Modified file saved as{output_filename}")

    except FileNotFoundError:
            print(f"Error:the file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error:You don't have permission to read '{input_filename}'.")
    except IOError as e:
         print(f"Error:An I/O error occured: {e}.")
    except Exception as e:
         print(f"An error occured: {e}.")
         #run the program
    if  __name__=="__main__":
       file_processor()