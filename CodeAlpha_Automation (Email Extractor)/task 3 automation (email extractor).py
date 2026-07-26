import re
import os

print("=== EMAIL EXTRACTOR ===")

input_file = input("Enter the path to your .txt file: ")

if not os.path.exists(input_file):
    print("File not found.")
else:
    file = open(input_file, "r")
    text = file.read()
    file.close()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    print("Found", len(emails), "emails.")

    if len(emails) > 0:
        print("Emails found:")
        for email in emails:
            print(email)

        output_file = input("Enter output file name (default: emails.txt): ")
        if output_file == "":
            output_file = "emails.txt"

        out = open(output_file, "w")
        for email in emails:
            out.write(email + "\n")
        out.close()

        print("Emails saved to", output_file)