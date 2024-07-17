import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error Type")
        return
    
    if not isinstance(attendees, list):
        print("Error Type")
        return
    
    if not template:
        print("template is empty")
        return
    
    if not attendees:
        print("No data provided")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        try:
            output_content = template
            for key in ['name', 'event_title', 'event_date', 'event_location']:
                value = attendee.get(key)
                if value is None:
                    value = 'N/A'
                placeholder = f"{{{key}}}"
                output_content = output_content.replace(placeholder, value)

            output_filename = f"output_{i}.txt"

            if os.path.exists(output_filename):
                print(f"Error: File {output_filename} already exists. Skipping.")
                continue

            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
                
            print(f"Generated {output_filename}")

        except Exception as  e:
            print(f"Error processing attendee {i}: {e}")

if __name__ == "__main__":
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt file not found.")
        template_content = ""