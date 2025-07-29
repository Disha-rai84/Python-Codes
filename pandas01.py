import pandas as pd

# students=[1,2,3,4,5]


# table = pd.Series(students,index = ["x", "y", "z","a","b"])

# print(table["a"])



# print(pd.__version__)




data = {
    "name": ["jhon","liz","ben","ash"],
    "ID": [102,123,104,105]
}

df = pd.DataFrame(data, index = ["student1","student2","student3","student4"])



print(df)
print(df.loc["student3"])
