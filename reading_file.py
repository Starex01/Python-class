# reading from a file
# use read() to read the entire file
# use readline() to read each line of the file
# use readlines() to read the entire file into a list, where each line is a list item
file = "bar.txt"
with open(file) as file_obj:
    contents = file_obj.readlines()
    print(contents)

# writing to a file
# You can write to a file using the write() method. If the file does not exist, it will be created. If it does exist, it will be overwritten.
file = "non_existent_file.txt"
with open(file, 'w') as file_obj:
    file_obj.write(f"Privacy Agreement\n We value your privacy and are committed to protecting your personal information. Any data you provide, including meter numbers and related details, is used solely to generate your electricity receipt and improve our services. We do not sell, share, or distribute your information to third parties without your consent, except where required by law. All data is handled securely and stored only for as long as necessary. By using this platform, you agree to the collection and use of your information in accordance with this policy. If you have any concerns, please contact us for clarification.")
    print(f"Privacy Agreement written to file {file}.")

# use writelines() to write multiple lines to a file. This method takes a list of strings and writes them to the file.
file = "names.txt"
with open(file, 'w') as file_obj:
    names = file_obj.writelines(["1. Alice\n", "2. Bob\n", "3. Charlie\n"])
    print(names)

