def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid arguments"
  formatted_name = f"{f_name} {l_name}".title()
  return formatted_name
