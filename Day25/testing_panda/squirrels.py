import pandas

extracted_data = {"Fur Color":[], "Count": []}
colors = ["Gray", "Cinnamon", "Black"]

data = pandas.read_csv("squirrel_data.csv")

for color in colors:
    extracted_data["Fur Color"].append(color)
    extracted_data["Count"].append(len(data[data["Primary Fur Color"] == color]))

pandas.DataFrame(extracted_data).to_csv("output.csv")

