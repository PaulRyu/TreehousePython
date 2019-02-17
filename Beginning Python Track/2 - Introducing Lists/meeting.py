attendees = ["Ken", "Alena", "Treasure"]
# attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently.")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)

print(to_line)
print(cc_line)

split_with_comma = to_line.split(", ")
not_split_with_comma = to_line.split()

print(split_with_comma)
print(not_split_with_comma)