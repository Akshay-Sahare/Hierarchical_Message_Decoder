
import os

def decode_message_from_file(file_name):
    print("-------Start Decoding from file-------------")

    if not os.path.exists(file_name):
        print(f"Error:,{file_name} file does not not found")
        return ""

    raw_data={}

    with open(file_name,'r') as file:
        lines= file.readlines()

    if not lines:
        print("Error , File is completly blank")
        return ""


    for line in lines:
        part=line.strip().split()
        if len(part)==2:
            number=int(part[0])
            word=part[1]
            raw_data[number]=word
        
      # sorting a data and creating a message
    sorted_numbers = sorted(raw_data.keys())
    decoded_words = [raw_data[num] for num in sorted_numbers]

    secret_message=" ".join(decoded_words)
    return secret_message

if __name__=="__main__":
    file_to_read="Raw_data.txt" 
    result=decode_message_from_file(file_to_read)
    if result:
        print(f"Decoded message is :-{result}")  